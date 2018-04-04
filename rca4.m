

cfgVHT = wlanVHTConfig;         
cfgVHT.ChannelBandwidth = 'CBW40'; % 80 MHz channel bandwidth
cfgVHT.MCS = 1;                    % 256-QAM 
cfgVHT.APEPLength = 4096;          % APEP length in bytes

% Set random stream for repeatability of results
s = rng(21);

%% Channel Configuration


tgacChannel = wlanTGacChannel;
tgacChannel.DelayProfile = 'Model-D';
tgacChannel.ChannelBandwidth = cfgVHT.ChannelBandwidth;
tgacChannel.NumTransmitAntennas = 1;
tgacChannel.NumReceiveAntennas = 1;
tgacChannel.TransmitReceiveDistance = 20; % Distance in meters for NLOS
tgacChannel.RandomStream = 'mt19937ar with seed';
tgacChannel.Seed = 10;

% Set the sampling rate for the channel
sr = wlanSampleRate(cfgVHT);
tgacChannel.SampleRate = sr;

%% Rate Control Algorithm Parameters


rcaAttack = 1;  % Control the sensitivity when MCS is increasing
rcaRelease = 0; % Control the sensitivity when MCS is decreasing
threshold = [11 14 19 20 25 28 30 31 35];
%threshold = [10 24 29 30 35 38 40 41 50];
snrUp = [threshold inf]+rcaAttack;
snrDown = [-inf threshold]-rcaRelease;
snrInd = cfgVHT.MCS; % Store the start MCS value

%% Simulation Parameters

numPackets = 100; % Number of packets transmitted during the simulation 
walkSNR = true; 

% Select SNR for the simulation
if walkSNR
    meanSNR = 22;   % Mean SNR
    amplitude = 14; % Variation in SNR around the average mean SNR value
    % Generate varying SNR values for each transmitted packet
    baseSNR = sin(linspace(1,10,numPackets))*amplitude+meanSNR;
    snrWalk = baseSNR(1); % Set the initial SNR value
    % The maxJump controls the maximum SNR difference between one
    % packet and the next 
    maxJump = 5;
else
    % Fixed mean SNR value for each transmitted packet. All the variability
    % in SNR comes from a time varying radio channel
    snrWalk = 22; %#ok<UNRCH>
end

% To plot the equalized constellation for each spatial stream set
% displayConstellation to true
displayConstellation = false;
if displayConstellation
    ConstellationDiagram = comm.ConstellationDiagram; %#ok<UNRCH>
    ConstellationDiagram.ShowGrid = true;
    ConstellationDiagram.Name = 'Equalized data symbols';
end

% Define simulation variables
snrMeasured = zeros(1,numPackets);
MCS = zeros(1,numPackets);
ber = zeros(1,numPackets);
packetLength = zeros(1,numPackets);

%% Processing Chain
%%


g_success = 0; % number of successful packet transmissions
g_timer = 0; % incremented for each packet transmitted irrespective of success or failure
g_recovery = false; % TRUE - when probing packet is just sent at higher rate else FALSE
g_success_threshold = 10;% number of successful transmissions required to send a probe packet
g_timeout = 15; % when timer reaches this value probe packet is sent
g_retry_threshold = 10; % number of consecutive failures required to drop this packet
g_min_success_threshold = min(threshold) ; % value used to initialize success_threshold when rate is dropped after two consecutive transmission failures
g_max_success_threshold = max(threshold) ; % maximum possible value of success_threshold
g_min_timeout = 15 ; % min value of timeout
g_success_k = 2 ; % multiplicative factor used to calculate new value of success_threshold when probe packet fails
g_timeout_k = 15 ; % set to min_timeout OR success_threshold x timeout_k
retry = 0;

%%% Process Chain %%%
for numPkt = 1:numPackets 
    if walkSNR
        % Generate SNR value per packet using random walk algorithm biased
        % towards the mean SNR
        snrWalk = 0.9*snrWalk+0.1*baseSNR(numPkt)+rand(1)*maxJump*2-maxJump;
    end
    
    %snrWalk = snr_eg(numPkt);
    % Generate a single packet waveform
    txPSDU = randi([0,1],8*cfgVHT.PSDULength,1,'int8');
    txWave = wlanWaveformGenerator(txPSDU,cfgVHT,'IdleTime',5e-4);
    
    % Receive processing, including SNR estimation
    y = processPacket(txWave,snrWalk,tgacChannel,cfgVHT);
          
    % Plot equalized symbols of data carrying subcarriers
    if displayConstellation && ~isempty(y.EstimatedSNR)
        release(ConstellationDiagram);
        ConstellationDiagram.ReferenceConstellation = helperReferenceSymbols(cfgVHT);
        ConstellationDiagram.Title = ['Packet ' int2str(numPkt)];
        ConstellationDiagram(y.EqDataSym(:));
        drawnow 
    end
    
    % Store estimated SNR value for each packet
    if isempty(y.EstimatedSNR) 
        snrMeasured(1,numPkt) = NaN;
    else
        snrMeasured(1,numPkt) = y.EstimatedSNR;
    end
    
    % Determine the length of the packet in seconds including idle time
    packetLength(numPkt) = y.RxWaveformLength/sr;
    
    % Calculate packet error rate (PER)
    if isempty(y.RxPSDU)
        % Set the PER of an undetected packet to NaN
        ber(numPkt) = NaN;
    else
        [~,ber(numPkt)] = biterr(y.RxPSDU,txPSDU);
    end

    % Compare the estimated SNR to the threshold, and adjust the MCS value
    % used for the next packet
     % Store current MCS value
    %status = txWave;
    MCS(numPkt) = cfgVHT.MCS;
    retry =0;    
    while (retry < g_retry_threshold)
        disp while;
        %status = send_packet(rxPSDU, cfgVHT.MCS);
        if ber(numPkt) == 0
            g_success = g_success + 1;
            retry = 0;
            disp if1;
                 if(g_success == g_success_threshold || g_timer == g_timeout) && cfgVHT.MCS ~= 9
                        increaseMCS = (mean(y.EstimatedSNR) > snrUp((snrInd==0)+ snrInd));   
                        disp increasedMCS;
                        snrInd = snrInd+increaseMCS;
                        cfgVHT.MCS = snrInd-1;
                         g_timer = 0;% incremented for each packet transmitted irrespective of success or failure
                         g_success = 0; % number of successful packet transmissions
                         g_recovery = true; % goes true when MCS is increased 
                        disp if2;
                 else 
                         g_timer = g_timer + 1 ;
                         g_recovery = false;
                        disp else2;
                         
                 end
                 break ;
        else 
            g_timer = g_timer + 1;
            retry = retry + 1;
            g_success = 0;
            disp else1;
            
             if g_recovery == false 
                
                 g_timer = 0;
               
                       if retry == 1 
                           g_success_threshold = min(g_success_threshold * g_success_k, g_max_success_threshold);
                           g_timeout = max(g_timeout_k * g_success_threshold,g_min_timeout);
                           disp if3;
                               if cfgVHT.MCS ~= 0
                               decreaseMCS = (mean(y.EstimatedSNR) <= snrDown((snrInd==0)+snrInd));
                               disp decreasedMCS;
                               snrInd = snrInd-decreaseMCS;
                               cfgVHT.MCS = snrInd-1;
                               end
                       end
            
            
           
            else (retry == 2 || retry == 4 || retry == 6 || retry == 8 || retry == 10)
                g_success_threshold = g_min_success_threshold;
                g_timeout = g_min_timeout;
                  if cfgVHT.MCS ~= 0
                      decreaseMCS = (mean(y.EstimatedSNR) <= snrDown((snrInd==0)+snrInd));
                      snrInd = snrInd+increaseMCS-decreaseMCS;
                        cfgVHT.MCS = snrInd-1;    
                        disp if4;
                  end
            end
        
                if retry > 2
                    g_timer=0;
                    disp if5;
                end
        end
%         snrInd = snrInd+increaseMCS;
%         cfgVHT.MCS = snrInd-1;
    end  
end
    

% snrInd = snrInd+increaseMCS-decreaseMCS;
% cfgVHT.MCS = snrInd-1;
%% Display and Plot Simulation Results


% Display and plot simulation results
disp(['Overall data rate: ' num2str(8*cfgVHT.APEPLength*(numPackets-numel(find(ber)))/sum(packetLength)/1e6) ' Mbps']);
disp(['Overall packet error rate: ' num2str(numel(find(ber))/numPackets)]);

plotResults(ber,packetLength,snrMeasured,MCS,cfgVHT);

% Restore default stream
rng(s);




function Y = processPacket(txWave,snrWalk,tgacChannel,cfgVHT)
    % Pass the transmitted waveform through the channel, perform
    % receiver processing, and SNR estimation.
    
    chanBW = cfgVHT.ChannelBandwidth; % Channel bandwidth
    % Set the following parameters to empty for an undetected packet
    estimatedSNR = [];
    eqDataSym = [];
    noiseVarVHT = [];
    rxPSDU = [];
    
    % Get the number of occupied subcarriers in VHT fields
    [vhtData,vhtPilots] = helperSubcarrierIndices(cfgVHT,'VHT');
    Nst_vht = numel(vhtData)+numel(vhtPilots);
    Nfft = helperFFTLength(cfgVHT); % FFT length
    
    % Pass the waveform through the fading channel model
    rxWave = tgacChannel(txWave);
    
    % Create an instance of the AWGN channel for each transmitted packet
    awgnChannel = comm.AWGNChannel;
    awgnChannel.NoiseMethod = 'Signal to noise ratio (SNR)';
    % Normalization
    awgnChannel.SignalPower = 1/tgacChannel.NumReceiveAntennas;
    % Account for energy in nulls
    awgnChannel.SNR = snrWalk-10*log10(Nfft/Nst_vht);
    
    % Add noise
    rxWave = awgnChannel(rxWave);
    rxWaveformLength = size(rxWave,1); % Length of the received waveform
    
    % Recover packet
    ind = wlanFieldIndices(cfgVHT); % Get field indices
    pktOffset = wlanPacketDetect(rxWave,chanBW); % Detect packet
    
    if ~isempty(pktOffset) % If packet detected
        % Extract the L-LTF field for fine timing synchronization
        LLTFSearchBuffer = rxWave(pktOffset+(ind.LSTF(1):ind.LSIG(2)),:);
    
        % Start index of L-LTF field
        finePktOffset = wlanSymbolTimingEstimate(LLTFSearchBuffer,chanBW);
     
        % Determine final packet offset
        pktOffset = pktOffset+finePktOffset;
        
        if pktOffset<15 % If synchronization successful
            % Extract L-LTF samples from the waveform, demodulate and
            % perform noise estimation
            LLTF = rxWave(pktOffset+(ind.LLTF(1):ind.LLTF(2)),:);
            demodLLTF = wlanLLTFDemodulate(LLTF,chanBW);

            % Estimate noise power in non-HT fields
            noiseVarVHT = helperNoiseEstimate(demodLLTF,chanBW,cfgVHT.NumSpaceTimeStreams,'Per Antenna');

            % Extract VHT-LTF samples from the waveform, demodulate and
            % perform channel estimation
            VHTLTF = rxWave(pktOffset+(ind.VHTLTF(1):ind.VHTLTF(2)),:);
            demodVHTLTF = wlanVHTLTFDemodulate(VHTLTF,cfgVHT);
            chanEstVHTLTF = wlanVHTLTFChannelEstimate(demodVHTLTF,cfgVHT);

            % Recover equalized symbols at data carrying subcarriers using
            % channel estimates from VHT-LTF
            [rxPSDU,~,eqDataSym] = wlanVHTDataRecover( ...
                rxWave(pktOffset + (ind.VHTData(1):ind.VHTData(2)),:), ...
                chanEstVHTLTF,mean(noiseVarVHT),cfgVHT);
            
            % SNR estimation per receive antenna
            powVHTLTF = mean(VHTLTF.*conj(VHTLTF));
            estSigPower = powVHTLTF-noiseVarVHT;
            estimatedSNR = 10*log10(mean(estSigPower./noiseVarVHT));
        end
    end
    
    % Set output
    Y = struct( ...
        'RxPSDU',           rxPSDU, ...
        'EqDataSym',        eqDataSym, ...
        'RxWaveformLength', rxWaveformLength, ...
        'NoiseVar',         noiseVarVHT, ...
        'EstimatedSNR',     estimatedSNR);
    
end

function plotResults(ber,packetLength,snrMeasured,MCS,cfgVHT)
    % Visualize simulation results

    figure('Outerposition',[50 50 900 700])
    subplot(4,1,1);
    plot(MCS);
    xlabel('Packet Number')
    ylabel('MCS')
    title('MCS selected for transmission')

    subplot(4,1,2);
    plot(snrMeasured);
    xlabel('Packet Number')
    ylabel('SNR')
    title('Estimated SNR')

    subplot(4,1,3);
    plot(find(ber==0),ber(ber==0),'x') 
    hold on; stem(find(ber>0),ber(ber>0),'or') 
    if any(ber)
        legend('Successful decode','Unsuccessful decode') 
    else
        legend('Successful decode') 
    end
    xlabel('Packet Number')
    ylabel('BER')
    title('Instantaneous bit error rate per packet')

    subplot(4,1,4);
    windowLength = 3; % Length of the averaging window
    movDataRate = movsum(8*cfgVHT.APEPLength.*(ber==0),windowLength)./movsum(packetLength,windowLength)/1e6;
    plot(movDataRate)
    xlabel('Packet Number')
    ylabel('Mbps')
    title(sprintf('Throughput over last %d packets',windowLength))
    
end