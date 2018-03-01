%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%% FM Receiver %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%following function is the implementation of an FM Receiver as a part of
%the lab exercise of Wireless Networking group WN01 made by Ninad Joshi and
%Dhaval Shah. This code can successfully capture a signal of a FM radio
%station and process it by using Decimator1,Discriminator, Decimator2 and
%a De-emphasis filter.

% Made By : Ninad Joshi & Dhaval Shah
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function fm_demod
rtlsdr_id        = '0';       % stick ID
rtlsdr_fc        = 102.7e6;   % tuner centre frequency in Hz
rtlsdr_gain      = 50;        % tuner gain in dB
rtlsdr_fs        = 2.4e6;     % tuner sampling rate
rtlsdr_ppm       = 0;         % tuner parts per million correction
rtlsdr_frmlen    = 512*25;    % output data frame size (multiple of 5)
rtlsdr_datatype  = 'single';  % output data type
audio_fs         = 48e3;      % audio output sampling rate
sim_time         = 60;        % simulation time in seconds
dec_fs1          = 240e3 ;     % sampling rate of decimator1


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%% CALCULATIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%%%%%%%%%%%%%%%%%%%%%%%% for de-emph filter%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% calculate time for 1 frame of data
rtlsdr_frmtime = rtlsdr_frmlen/rtlsdr_fs; 


% find de-emphasis filter coeff
[num,den] = butter(1,3183.1/(audio_fs/2)); 
%butterworth low-pass filter is implemented with an order of 1 and
%frequency as shown above. 
%[Reference : from the rtl-sdr book]


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%% SYSTEM OBJECTS%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   

%%%%%%%%%%%%%%%%%%%%%%% link to a physical rtl-sdr%%%%%%%%%%%%%%%%%%%%%%%%%
    %receives data from SDR device can have many parameters
    obj_rtlsdr = comm.SDRRTLReceiver(...
        rtlsdr_id,...
        'CenterFrequency', rtlsdr_fc,...
        'EnableTunerAGC', false,...
        'TunerGain', rtlsdr_gain,...
        'SampleRate', rtlsdr_fs, ...
        'SamplesPerFrame', rtlsdr_frmlen,...
        'OutputDataType', rtlsdr_datatype,...
        'FrequencyCorrection', rtlsdr_ppm);
    
    
%%%%%%%%%%%%%%%%%%%%%%%%%% FIR Decimator %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Decimator is a combination of an FIR Low Pass filter and a Downsampler
    
    
% with decimation factor = 10 placed after SDR having
 % a Windowed FIR with a order 63 (ref lab6 5.3 Q1-c)
  %%%% fir1 function is used for windowed fir %%%%  
    obj_decmtr0 = dsp.FIRDecimator(...
        'DecimationFactor', 10,...
        'Numerator', fir1(63,0.07));
    %%% for low pass with window is chosen fir1 function 
    % the cut-off frequency is -3db of the peak value = 0.03MHz
    % % f[radian/sample] = (0.03MHz * 2pi)/rtlsdr_fs = 0.07 rad/samples
    

    %  with decimation factor = 5 placed after the discriminator
    obj_decmtr1 = dsp.FIRDecimator(...
        'DecimationFactor', 5,...
        'Numerator', fir1(63,0.005));
    % fir1 is a function that takes no. of taps and cut-off frquency in rad/sample
    % parameters no. of taps = 63 (given)
    %for the frequency we were given with a frequency of 48 ksps 
    % f[radian/sample] = (0.2KHz * 2pi)/dec_fs1 = 0.005 rad/samples
    

%%%%%%%%%%%%%%%%%%%%% IIR De-Emphasis Filter%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

obj_deemph = dsp.IIRFilter(...
    'Numerator', num,...
    'Denominator', den);

% delay
obj_delay = dsp.Delay;
%%%delay is being provided

% audio output
obj_audio = dsp.AudioPlayer(audio_fs);


%%%%%%%%%%%%%%%%%%%%%%% spectrum analyzers%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%% There are spectrum analysers used one for demodulated signal 
%parameters of the spectrum specified [ref. Matlab Help + rtl-sdr book]
%%%generated after de-emphesis filter and other for
%%% modulated signal received by RTL-SDR %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% spectrum analyser for modulated signal received by rtl-sdr
obj_spectrummod   = dsp.SpectrumAnalyzer(...
    'Name', 'Spectrum Analyzer Modulated',...
    'Title', 'Spectrum Analyzer Modulated',...
    'SpectrumType', 'Power density',...
    'FrequencySpan', 'Full',...
    'SampleRate', rtlsdr_fs);

%spectrum analyser for the demodulated signal at output
obj_spectrumdemod = dsp.SpectrumAnalyzer(...
    'Name', 'Spectrum Analyzer Demodulated',...
    'Title', 'Spectrum Analyzer Demodulated',...
    'SpectrumType', 'Power density',...
    'FrequencySpan', 'Full',...
    'SampleRate', audio_fs);

% spectrum anlyser for the decimator1 
obj_spectrumdeci1 = dsp.SpectrumAnalyzer(...
    'Name', 'Spectrum Analyzer Decimator1',...
    'Title', 'Spectrum Analyzer Decimator1',...
    'SpectrumType', 'Power density',...
    'FrequencySpan', 'Full',...
    'SampleRate', dec_fs1);
%spectrum analyser for discriminator
obj_spectrumdisc = dsp.SpectrumAnalyzer(...
    'Name', 'Spectrum Analyzer Discriminator',...
    'Title', 'Spectrum Analyzer Discriminator',...
    'SpectrumType', 'Power density',...
    'FrequencySpan', 'Full',...
    'SampleRate', dec_fs1);



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%% SIMULATION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% if using RTL-SDR, check first if RTL-SDR is active otherwise shows error
   
    if ~isempty(sdrinfo(obj_rtlsdr.RadioAddress))
    else
        error(['RTL-SDR failure. Please check connection to ',...
            'MATLAB using the "sdrinfo" command.']);
    end


% reset run_time to 0 (secs)
run_time = 0;

% loop while run_time is less than sim_time
while run_time < sim_time
    
    %%%%%%%%%%%% fetch a frame from obj_rtlsdr %%%%%%%%%%%%%%%%%%%%%%%%%%%%
    rtlsdr_data = step(obj_rtlsdr);
    
    %%%%% update 'modulated' spectrum analyzer window with new data %%%%%%%
    step(obj_spectrummod, rtlsdr_data);
    
    
    %%%%%%%%%%%%%%%%%% Implement decimator%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    
    data_dec0 = step(obj_decmtr0,rtlsdr_data);
    
    step(obj_spectrumdeci1,dec_fs1); 
    % step function is used to read the data from the input file
    
    %%%%%%%%%%%% implement frequency discriminator%%%%%%%%%%%%%%%%%%%%%%%%%
    
    
    % converts frequency change to amplitude change by taking input from
    % the second decimator
    
    % Discriminator is a combination of a math function, delay, product and
    % angle blocks of a dsp toolbox.
    
    discrim_delay = step(obj_delay,data_dec0); 
    % delay block is implemented
    discrim_conj  = conj(data_dec0); 
    % conjugate (math block) is implemented
    discrim_pd    = discrim_delay.*discrim_conj;
    % product block is implemented
    discrim_arg   = angle(discrim_pd); 
    % anular block is implemented
    
    step(obj_spectrumdisc,discrim_arg)
    
    %%%%%%%%%%%%%%%%%% Implement decimator%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    data_dec1 = step(obj_decmtr1,discrim_arg);
   
    
    %%%%%%%%%%%%%% Implement De-emphasis filter data*********************
    data_deemph = step(obj_deemph,data_dec1);
    
    %%%% update 'demodulated' spectrum analyzer window with new data%%%%%%
    
    step(obj_spectrumdemod, data_deemph);
    
    
    %%%%%%%%%%%%% output demodulated signal to speakers%%%%%%%%%%%%%%%%%%%%
    step(obj_audio,data_deemph);
    
    %%%%%%%%%%%% update run_time after processing another frame%%%%%%%%%%%%
    run_time = run_time + rtlsdr_frmtime;
    
end

end
