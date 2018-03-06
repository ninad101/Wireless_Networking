#!/usr/bin/env python
import csv
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

homeOne = open("home1.txt", "r")
homeTwo = open("home2.txt", "r")
homeThree = open("home3.txt", "r")
homeFour = open("home4.txt", "r")

delftaccOne = open("delftacc1.txt", "r")
delftaccTwo = open("delftacc2.txt","r")
delftaccThree = open("delftacc3.txt", "r")
delftaccFour = open("delftacc4.txt", "r")

delftOne = open("delft1.txt", "r")

campusOne = open("campus1.txt", "r")
campusTwo = open("campus2.txt", "r")
campusThree = open("campus3.txt", "r")

csvReader1 = csv.reader(homeOne)
header1 = csvReader1.next()
cckIndex1 = header1.index("Complementary Code Keying (CCK)")
datarateIndex1 = header1.index("Data rate")
ofdmIndex1 = header1.index("Orthogonal Frequency-Division Multiplexing (OFDM)")
gfskIndex1 = header1.index("Gaussian Frequency Shift Keying (GFSK)")
dynamicIndex1 = header1.index("Dynamic CCK-OFDM")
mcsIndex1 = header1.index("MCS index")
PHYIndex1 = header1.index("PHY type")

csvReader2 = csv.reader(homeTwo)
header2 = csvReader2.next()
cckIndex2 = header2.index("Complementary Code Keying (CCK)")
datarateIndex2 = header2.index("Data rate")
ofdmIndex2 = header2.index("Orthogonal Frequency-Division Multiplexing (OFDM)")
gfskIndex2 = header2.index("Gaussian Frequency Shift Keying (GFSK)")
dynamicIndex2 = header2.index("Dynamic CCK-OFDM")
mcsIndex2 = header2.index("MCS index")
PHYIndex2 = header2.index("PHY type")

csvReader3 = csv.reader(homeThree)
header3 = csvReader3.next()
cckIndex3 = header3.index("Complementary Code Keying (CCK)")
datarateIndex3 = header3.index("Data rate")
ofdmIndex3 = header3.index("Orthogonal Frequency-Division Multiplexing (OFDM)")
gfskIndex3 = header3.index("Gaussian Frequency Shift Keying (GFSK)")
dynamicIndex3 = header3.index("Dynamic CCK-OFDM")
mcsIndex3 = header3.index("MCS index")
PHYIndex3 = header3.index("PHY type")

csvReader4 = csv.reader(homeFour)
header4 = csvReader4.next()
cckIndex4 = header4.index("Complementary Code Keying (CCK)")
datarateIndex4 = header4.index("Data rate")
ofdmIndex4 = header4.index("Orthogonal Frequency-Division Multiplexing (OFDM)")
gfskIndex4 = header4.index("Gaussian Frequency Shift Keying (GFSK)")
dynamicIndex4 = header4.index("Dynamic CCK-OFDM")
mcsIndex4 = header4.index("MCS index")
PHYIndex4 = header4.index("PHY type")

csvReader5 = csv.reader(delftaccOne)
header5 = csvReader5.next()
cckIndex5 = header5.index("Complementary Code Keying (CCK)")
datarateIndex5 = header5.index("Data rate")
ofdmIndex5 = header5.index("Orthogonal Frequency-Division Multiplexing (OFDM)")
gfskIndex5 = header5.index("Gaussian Frequency Shift Keying (GFSK)")
dynamicIndex5 = header5.index("Dynamic CCK-OFDM")
mcsIndex5 = header5.index("MCS index")
PHYIndex5 = header5.index("PHY type")

csvReader6 = csv.reader(delftaccTwo)
header6 = csvReader6.next()
cckIndex6 = header6.index("Complementary Code Keying (CCK)")
datarateIndex6 = header6.index("Data rate")
ofdmIndex6 = header6.index("Orthogonal Frequency-Division Multiplexing (OFDM)")
gfskIndex6 = header6.index("Gaussian Frequency Shift Keying (GFSK)")
dynamicIndex6 = header6.index("Dynamic CCK-OFDM")
mcsIndex6 = header6.index("MCS index")
PHYIndex6 = header6.index("PHY type")

csvReader7 = csv.reader(delftaccThree)
header7 = csvReader7.next()
cckIndex7 = header7.index("Complementary Code Keying (CCK)")
datarateIndex7 = header7.index("Data rate")
ofdmIndex7 = header7.index("Orthogonal Frequency-Division Multiplexing (OFDM)")
gfskIndex7 = header7.index("Gaussian Frequency Shift Keying (GFSK)")
dynamicIndex7 = header7.index("Dynamic CCK-OFDM")
mcsIndex7 = header7.index("MCS index")
PHYIndex7 = header7.index("PHY type")

csvReader8 = csv.reader(delftaccFour)
header8 = csvReader8.next()
cckIndex8 = header8.index("Complementary Code Keying (CCK)")
datarateIndex8 = header8.index("Data rate")
ofdmIndex8 = header8.index("Orthogonal Frequency-Division Multiplexing (OFDM)")
gfskIndex8 = header8.index("Gaussian Frequency Shift Keying (GFSK)")
dynamicIndex8 = header8.index("Dynamic CCK-OFDM")
mcsIndex8 = header8.index("MCS index")
PHYIndex8 = header8.index("PHY type")

csvReader9 = csv.reader(delftOne)
header9 = csvReader9.next()
cckIndex9 = header9.index("Complementary Code Keying (CCK)")
datarateIndex9 = header9.index("Data rate")
ofdmIndex9 = header9.index("Orthogonal Frequency-Division Multiplexing (OFDM)")
gfskIndex9 = header9.index("Gaussian Frequency Shift Keying (GFSK)")
dynamicIndex9 = header9.index("Dynamic CCK-OFDM")
mcsIndex9 = header9.index("MCS index")
PHYIndex9 = header9.index("PHY type")

csvReader10 = csv.reader(campusOne)
header10 = csvReader10.next()
cckIndex10 = header10.index("Complementary Code Keying (CCK)")
datarateIndex10 = header10.index("Data rate")
ofdmIndex10 = header10.index("Orthogonal Frequency-Division Multiplexing (OFDM)")
gfskIndex10 = header10.index("Gaussian Frequency Shift Keying (GFSK)")
dynamicIndex10 = header10.index("Dynamic CCK-OFDM")
mcsIndex10 = header10.index("MCS index")
PHYIndex10 = header10.index("PHY type")

csvReader11 = csv.reader(campusTwo)
header11 = csvReader11.next()
cckIndex11 = header11.index("Complementary Code Keying (CCK)")
datarateIndex11 = header11.index("Data rate")
ofdmIndex11 = header11.index("Orthogonal Frequency-Division Multiplexing (OFDM)")
gfskIndex11 = header11.index("Gaussian Frequency Shift Keying (GFSK)")
dynamicIndex11 = header11.index("Dynamic CCK-OFDM")
mcsIndex11 = header11.index("MCS index")
PHYIndex11 = header11.index("PHY type")

csvReader12 = csv.reader(campusThree)
header12 = csvReader12.next()
cckIndex12 = header12.index("Complementary Code Keying (CCK)")
datarateIndex12 = header12.index("Data rate")
ofdmIndex12 = header12.index("Orthogonal Frequency-Division Multiplexing (OFDM)")
gfskIndex12 = header12.index("Gaussian Frequency Shift Keying (GFSK)")
dynamicIndex12 = header12.index("Dynamic CCK-OFDM")
mcsIndex12 = header12.index("MCS index")
PHYIndex12 = header12.index("PHY type")

homelistdatarate = []																	#list containing datarates of all packets
homelistphy = []																		#list containing PHY type of all packets
homelistcck = []																		#list containing cck value of all packets
homelistofdm = []																		#list containing ofdm value of all packets
homelistgfsk = []																		#list containing gfsk values of all packets
homelistdynamic = []																	#list containing dynamic values of all packets
homelistmcs = []																		#list containing mcsindex of all packets

acclistdatarate = []																	#list containing datarates of all packets
acclistphy = []																			#list containing PHY type of all packets
acclistcck = []																			#list containing cck value of all packets
acclistofdm = []																		#list containing ofdm value of all packets
acclistgfsk = []																		#list containing gfsk values of all packets
acclistdynamic = []																		#list containing dynamic values of all packets
acclistmcs = []																			#list containing mcsindex of all packets

delftlistdatarate = []																	#list containing datarates of all packets
delftlistphy = []																		#list containing PHY type of all packets
delftlistcck = []																		#list containing cck value of all packets
delftlistofdm = []																		#list containing ofdm value of all packets
delftlistgfsk = []																		#list containing gfsk values of all packets
delftlistdynamic = []																	#list containing dynamic values of all packets
delftlistmcs = []																		#list containing mcsindex of all packets

camplistdatarate = []																	#list containing datarates of all packets
camplistphy = []																		#list containing PHY type of all packets
camplistcck = []																		#list containing cck value of all packets
camplistofdm = []																		#list containing ofdm value of all packets
camplistgfsk = []																		#list containing gfsk values of all packets
camplistdynamic = []																	#list containing dynamic values of all packets
camplistmcs = []																		#list containing mcsindex of all packets

for row in csvReader1:
	homecck = row[cckIndex1]
	homedatarate = row[datarateIndex1]
	homeofdm = row[ofdmIndex1]
	homegfsk = row[gfskIndex1]
	homedynamic = row[dynamicIndex1]
	homemcs = row[mcsIndex1]
	homephy = row[PHYIndex1]
	homelistdatarate.append([homedatarate])
	homelistphy.append([homephy])
	homelistcck.append([homecck])
	homelistofdm.append([homeofdm])
	homelistgfsk.append([homegfsk])
	homelistdynamic.append([homedynamic])
	homelistmcs.append([homemcs])


for row in csvReader2:
	cck = row[cckIndex2]
	datarate = row[datarateIndex2]
	ofdm = row[ofdmIndex2]
	gfsk = row[gfskIndex2]
	dynamic = row[dynamicIndex2]
	mcs = row[mcsIndex2]
	phy = row[PHYIndex2]
	homelistdatarate.append([homedatarate])
	homelistphy.append([homephy])
	homelistcck.append([homecck])
	homelistofdm.append([homeofdm])
	homelistgfsk.append([homegfsk])
	homelistdynamic.append([homedynamic])
	homelistmcs.append([homemcs])

for row in csvReader3:
	cck = row[cckIndex3]
	datarate = row[datarateIndex3]
	ofdm = row[ofdmIndex3]
	gfsk = row[gfskIndex3]
	dynamic = row[dynamicIndex3]
	mcs = row[mcsIndex3]
	phy = row[PHYIndex3]
	homelistdatarate.append([homedatarate])
	homelistphy.append([homephy])
	homelistcck.append([homecck])
	homelistofdm.append([homeofdm])
	homelistgfsk.append([homegfsk])
	homelistdynamic.append([homedynamic])
	homelistmcs.append([homemcs])

for row in csvReader4:
	cck = row[cckIndex4]
	datarate = row[datarateIndex4]
	ofdm = row[ofdmIndex4]
	gfsk = row[gfskIndex4]
	dynamic = row[dynamicIndex4]
	mcs = row[mcsIndex4]
	phy = row[PHYIndex4]
	homelistdatarate.append([homedatarate])
	homelistphy.append([homephy])
	homelistcck.append([homecck])
	homelistofdm.append([homeofdm])
	homelistgfsk.append([homegfsk])
	homelistdynamic.append([homedynamic])
	homelistmcs.append([homemcs])

for row in csvReader5:
	cck = row[cckIndex5]
	datarate = row[datarateIndex5]
	ofdm = row[ofdmIndex5]
	gfsk = row[gfskIndex5]
	dynamic = row[dynamicIndex5]
	mcs = row[mcsIndex5]
	phy = row[PHYIndex5]
	acclistdatarate.append([datarate])
	acclistphy.append([phy])
	acclistcck.append([cck])
	acclistofdm.append([ofdm])
	acclistgfsk.append([gfsk])
	acclistdynamic.append([dynamic])
	acclistmcs.append([mcs])


for row in csvReader6:
	cck = row[cckIndex6]
	datarate = row[datarateIndex6]
	ofdm = row[ofdmIndex6]
	gfsk = row[gfskIndex6]
	dynamic = row[dynamicIndex6]
	mcs = row[mcsIndex6]
	phy = row[PHYIndex6]
	acclistdatarate.append([datarate])
	acclistphy.append([phy])
	acclistcck.append([cck])
	acclistofdm.append([ofdm])
	acclistgfsk.append([gfsk])
	acclistdynamic.append([dynamic])
	acclistmcs.append([mcs])

for row in csvReader7:
	cck = row[cckIndex7]
	datarate = row[datarateIndex7]
	ofdm = row[ofdmIndex7]
	gfsk = row[gfskIndex7]
	dynamic = row[dynamicIndex7]
	mcs = row[mcsIndex7]
	phy = row[PHYIndex7]
	acclistdatarate.append([datarate])
	acclistphy.append([phy])
	acclistcck.append([cck])
	acclistofdm.append([ofdm])
	acclistgfsk.append([gfsk])
	acclistdynamic.append([dynamic])
	acclistmcs.append([mcs])

for row in csvReader8:
	cck = row[cckIndex8]
	datarate = row[datarateIndex8]
	ofdm = row[ofdmIndex8]
	gfsk = row[gfskIndex8]
	dynamic = row[dynamicIndex8]
	mcs = row[mcsIndex8]
	phy = row[PHYIndex8]
	acclistdatarate.append([datarate])
	acclistphy.append([phy])
	acclistcck.append([cck])
	acclistofdm.append([ofdm])
	acclistgfsk.append([gfsk])
	acclistdynamic.append([dynamic])
	acclistmcs.append([mcs])

for row in csvReader10:
	cck = row[cckIndex10]
	datarate = row[datarateIndex10]
	ofdm = row[ofdmIndex10]
	gfsk = row[gfskIndex10]
	dynamic = row[dynamicIndex10]
	mcs = row[mcsIndex10]
	phy = row[PHYIndex10]
	camplistdatarate.append([datarate])
	camplistphy.append([phy])
	camplistcck.append([cck])
	camplistofdm.append([ofdm])
	camplistgfsk.append([gfsk])
	camplistdynamic.append([dynamic])
	camplistmcs.append([mcs])


for row in csvReader11:
	cck = row[cckIndex11]
	datarate = row[datarateIndex11]
	ofdm = row[ofdmIndex11]
	gfsk = row[gfskIndex11]
	dynamic = row[dynamicIndex11]
	mcs = row[mcsIndex11]
	phy = row[PHYIndex11]
	camplistdatarate.append([datarate])
	camplistphy.append([phy])
	camplistcck.append([cck])
	camplistofdm.append([ofdm])
	camplistgfsk.append([gfsk])
	camplistdynamic.append([dynamic])
	camplistmcs.append([mcs])

for row in csvReader12:
	cck = row[cckIndex12]
	datarate = row[datarateIndex12]
	ofdm = row[ofdmIndex12]
	gfsk = row[gfskIndex12]
	dynamic = row[dynamicIndex12]
	mcs = row[mcsIndex12]
	phy = row[PHYIndex12]
	camplistdatarate.append([datarate])
	camplistphy.append([phy])
	camplistcck.append([cck])
	camplistofdm.append([ofdm])
	camplistgfsk.append([gfsk])
	camplistdynamic.append([dynamic])
	camplistmcs.append([mcs])

homelistb = []  																	#listt of indexes of PHYB
homelistphybmcs = [] 																#list of mcs for PHYB
homelistphybcck = []																#list of cck value for PHYB
homelistphybofdm = []																#list of ofdm value for PHYB
homelistphybgfsk = []																#list of gfsk value for PHYB
homelistphybdynamic = []															#list of dynamic value for PHYB
homelistphybdatarate = []															#list of datarate for PHYB

for i,j in enumerate(homelistphy):
	if str(j[0]) == '802.11b':
#		print i
#		listb.append([i])
		homelistphybmcs.append(homelistmcs[i])
		homelistphybcck.append(homelistcck[i])
		homelistphybofdm.append(homelistofdm[i])
		homelistphybgfsk.append(homelistgfsk[i])
		homelistphybdynamic.append(homelistdynamic[i])
		homelistphybdatarate.append(homelistdatarate[i])

#print homelistphybdatarate
#print homelistphybofdm

#homelistphybofdmdatarate = []														#list of ofdm datarates for phyb


homekhaalilist = []																	#list to check CCk in PHYB

for item in homelistphybcck:
	if str(item[0]) not in homekhaalilist:
		homekhaalilist.append(str(item[0]))

#print homekhaalilist
#print "Since we only have True for CCK, it means no other modulation types are present for PHYB at home in India"

homelistg = []  																	#listt of indexes of PHYG
homelistphygofdm = []																#list of ofdm value for PHYG
homelistphygdatarate = []															#list of datarate for PHYG

for i,j in enumerate(homelistphy):
	if str(j[0]) == '802.11g':
#		print i
#		listb.append([i])
		homelistphygofdm.append(homelistofdm[i])
		homelistphygdatarate.append(homelistdatarate[i])

#print homelistphygofdm
#print homelistphygdatarate

drphyb1 = [1,2]																		#PHYB datarate = 1
#drphyb2 = 2																		#PHYB having datarate = 2
drphyg6 = [0,6]																		#PHYG datarate = 6

#print ('The number of packets with Data Rate = 1 and PHY type 802.11b are: %d ' %drphyb1)
#print ('The number of packets with Data Rate = 1 and PHY type 802.11b are: %d ' %drphyb2)

#avgphybhomedr = 0																#average datarate for PHYB packets in India home

#avgphybhomedr = (drphyb1 + 2*drphyb2)/(drphyb1 + drphyb2)
#print avgphybhomedr

#a = [drphyb1,drphyb2,drphyg6]															#Plot for Data Rates for PHY type 802.11b in India
#x = np.arange(len(a))
#name = ('802.11b CCK' ,'', '802.11g OFDM')
#fig1 = plt.figure(1)
#bar = plt.bar(x,a)
#bar[2].set_color('r')
#plt.xticks(x,name)
#plt.title('Data Rates for PHY type 802.11b and 802.11g in India ')
#plt.ylabel('Data Rate')
#fig1.show()

homelistn = []  																	#listt of indexes of PHYN
homelistphynmcs = [] 																#list of mcs for PHYN
homelistphyncck = []																#list of cck value for PHYN
homelistphynofdm = []																#list of ofdm value for PHYN
homelistphyngfsk = []																#list of gfsk value for PHYN
homelistphyndynamic = []															#list of dynamic value for PHYN
homelistphyndatarate = []															#list of datarate for PHYN

for i,j in enumerate(homelistphy):
	if str(j[0]) == '802.11n':
#		print i
#		listb.append([i])
		homelistphynmcs.append(homelistmcs[i])
		homelistphyncck.append(homelistcck[i])
		homelistphynofdm.append(homelistofdm[i])
		homelistphyngfsk.append(homelistgfsk[i])
		homelistphyndynamic.append(homelistdynamic[i])
		homelistphyndatarate.append(homelistdatarate[i])

homekhaalilist1 = []
homekhaalilist2 = []

for i,j in enumerate(homelistphynmcs):
	if str(j[0]) != ' ':
		homekhaalilist1.append(homelistphynmcs[i])
		homekhaalilist2.append(homelistphyndatarate[i])


#print khaalilist1
#print khaalilist2

homelistcheckelement = []															#list to check unique mcs index in PHYN
homelistcheckelement1 = []															#list to check unnique values of datarates in PHYN		

for item in homelistphynmcs:
	if str(item[0]) not in homelistcheckelement:
		homelistcheckelement.append(str(item[0]))

#print listcheckelement

for item in homelistphyndatarate:
	if str(item[0]) not in homelistcheckelement1:
		homelistcheckelement1.append(str(item[0]))
#print "Unique values of datarates in PHYN in India are: "
#print listcheckelement1

homelistdrphyn15 = []
homelistdrphyn14 = []
homelistdrphyn13 = []
homelistdrphyn12 = []
homelistdrphyn10 = []
homelistdrphyn7 = []
homelistdrphyn4 = []
homelistdrphyn3 = []
homelistdrphyn6 = []

for i,j in enumerate(homelistphynmcs):
	if str(j[0]) == '15':
		homelistdrphyn15.append(homelistphyndatarate[i])
	elif str(j[0]) == '14':
		homelistdrphyn14.append(homelistphyndatarate[i])
	elif str(j[0]) == '13':
		homelistdrphyn13.append(homelistphyndatarate[i])
	elif str(j[0]) == '7':
		homelistdrphyn7.append(homelistphyndatarate[i])
	elif str(j[0]) == '12':
		homelistdrphyn12.append(homelistphyndatarate[i])
	elif str(j[0]) == '10':
		homelistdrphyn10.append(homelistphyndatarate[i])
	elif str(j[0]) == '4':
		homelistdrphyn4.append(homelistphyndatarate[i])
	elif str(j[0]) == '3':
		homelistdrphyn3.append(homelistphyndatarate[i])
	elif str(j[0]) == '6':
		homelistdrphyn3.append(homelistphyndatarate[i])	
#print listdrphyn15
print "Due to comma being used instead of a decimal point, the datarates cannot be typecast into int/float. Hence we extract unique values of them and add them manually to a list "

yaxisphynhome = [144.444, 130, 117, 115.556, 104, 72.2222, 65, 58.5, 78, 43.3333, 39, 26, 39]  #Yaxis for datarate vs mod type for PHYN in India
namephynhome = ['','','','','64-QAM','','','','','16-QAM','','','QPSK']
xaxisphynhome = np.arange(len(yaxisphynhome))
fig2 = plt.figure(2)
barline = plt.bar(xaxisphynhome,yaxisphynhome)
barline[0].set_color('r')
barline[1].set_color('r')
barline[2].set_color('r')
barline[3].set_color('r')
barline[4].set_color('r')
barline[5].set_color('r')
barline[6].set_color('r')
barline[7].set_color('r')
barline[8].set_color('g')
barline[9].set_color('g')
barline[10].set_color('g')
barline[11].set_color('g')

plt.title('Data Rates vs Modulation types for PHY type 802.11n in India')
plt.ylabel('Data Rate')
plt.xticks(xaxisphynhome,namephynhome)
fig2.show ()

homelistdrphyndynamic = []

for i,j in enumerate(homelistphyndynamic):
	if str(j[0]) == 'True':
		homelistdrphyndynamic.append(homelistphyndatarate[i])

#print listdrphyndynamic

homelistscheckelement = []

for item in homelistdrphyndynamic:
	if str(item[0]) not in homelistscheckelement:
		homelistscheckelement.append(str(item[0]))

#print homelistscheckelement

phyndynamicyaxis = [26,39, 43.3333, 65, 72.2222, 78, 117, 130]
phyndynamicxaxis = np.arange(len(phyndynamicyaxis))
fig3 = plt.figure(3)
plot(phyndynamicxaxis,phyndynamicyaxis)
title('Data Rates vs Modulation types for PHY type 802.11n in India (OFDM-CCK)')
ylabel("Data Rates")
xlabel("Items")
fig3.show ()

acclistnew = []																		#check PHY types

#for item in listphy:
#	if str(item[0]) not in listnew:
#		listnew.append(str(item[0]))

#print listnew

acclistb = []  																		#list of indexes of PHYG
acclistphygofdm = []																#list of ofdm value for PHYG
acclistphygdatarate = []															#list of datarate for PHYG

for i,j in enumerate(acclistphy):
	if str(j[0]) == '802.11g':
#		print i
#		acclistb.append([i])
		acclistphygofdm.append(acclistofdm[i])
		acclistphygdatarate.append(acclistdatarate[i])

#print acclistphygofdm
#print acclistphygdatarate

listdrphygofdm = []

for i,j in enumerate(acclistphygofdm):
	if str(j[0]) == 'True':
		listdrphygofdm.append(acclistphygdatarate[i])

#print listdrphyndynamic

accphygofdmyaxis = [6,9,12,18,24,36,48,54]
accphygofdmxaxis = np.arange(len(accphygofdmyaxis))
fig4 = plt.figure(4)
plot(accphygofdmxaxis,accphygofdmyaxis)
ylabel('Data Rates')
title('Data Rates vs Modulation types for PHY type 802.11g in Delft (Dorm) (OFDM)')
#fig4.show ()

acclistb = []  																		#list of indexes of PHYB
acclistphybmcs = [] 																#list of mcs for PHYB
acclistphybcck = []																	#list of cck value for PHYB
acclistphybofdm = []																#list of ofdm value for PHYB
acclistphybgfsk = []																#list of gfsk value for PHYB
acclistphybdynamic = []																#list of dynamic value for PHYB
acclistphybdatarate = []															#list of datarate for PHYB

for i,j in enumerate(acclistphy):
	if str(j[0]) == '802.11b':
#		print i
#		acclistb.append([i])
		acclistphybmcs.append(acclistmcs[i])
		acclistphybcck.append(acclistcck[i])
		acclistphybofdm.append(acclistofdm[i])
		acclistphybgfsk.append(acclistgfsk[i])
		acclistphybdynamic.append(acclistdynamic[i])
		acclistphybdatarate.append(acclistdatarate[i])

#print acclistphybdatarate
#print acclistphybofdm

#acclistphybofdmdatarate = []														#list of ofdm datarates for phyb


acckhaalilist = []																	#list to check CCk in PHYB

for item in acclistphybdatarate:
	if str(item[0]) not in acckhaalilist:
		acckhaalilist.append(str(item[0]))

#print acckhaalilist

accphybcckyaxis = [1,2,5.5,11]
accphybcckxaxis = np.arange(len(accphybcckyaxis))
fig5 = plt.figure(5)
plot(accphybcckxaxis,accphybcckyaxis)
ylabel('Data Rates')
title('Data Rates vs Modulation types for PHY type 802.11b in Delft (Dorm) (CCK)')
#fig5.show ()

acclistd = []  																		#list of indexes of PHYB
acclistphydmcs = [] 																#list of mcs for PHYB
acclistphydcck = []																	#list of cck value for PHYB
acclistphydofdm = []																#list of ofdm value for PHYB
acclistphydgfsk = []																#list of gfsk value for PHYB
acclistphyddynamic = []																#list of dynamic value for PHYB
acclistphyddatarate = []															#list of datarate for PHYB

for i,j in enumerate(acclistphy):
	if str(j[0]) == '802.11 DSSS':
#		print i
#		acclistd.append([i])
		acclistphydmcs.append(acclistmcs[i])
		acclistphydcck.append(acclistcck[i])
		acclistphydofdm.append(acclistofdm[i])
		acclistphydgfsk.append(acclistgfsk[i])
		acclistphyddynamic.append(acclistdynamic[i])
		acclistphyddatarate.append(acclistdatarate[i])

#print acclistphybdatarate
#print acclistphybofdm

#acclistphybofdmdatarate = []														#list of ofdm datarates for phy DSSS

#print acclistphyddatarate
acckhaalilist1 = []																	#list to check CCk in DSSS

for item in acclistphyddatarate:
	if str(item[0]) not in acckhaalilist1:
		acckhaalilist1.append(str(item[0]))

#print acckhaalilist1
print 'Data Rates for 802.11 DSSS are not available on wireshark'

delftlistnew = []																		#check PHY types

#for item in delftlistphy:
#	if str(item[0]) not in delftlistnew:
#		delftlistnew.append(str(item[0]))

#print delftlistnew

delftlistb = []  																	#listt of indexes of PHYG
delftlistphygofdm = []																#list of ofdm value for PHYG
delftlistphygdatarate = []															#list of datarate for PHYG

for i,j in enumerate(delftlistphy):
	if str(j[0]) == '802.11g':
#		print i
#		delftlistb.append([i])
		delftlistphygofdm.append(delftlistofdm[i])
		delftlistphygdatarate.append(delftlistdatarate[i])

#print delftlistphygofdm
#print delftlistphygdatarate

delftlistdrphygofdm = []

for i,j in enumerate(delftlistphygofdm):
	if str(j[0]) == 'True':
		delftlistdrphygofdm.append(delftlistphygdatarate[i])

#print delftlistdrphygofdm

delftphygofdmyaxis = [6,9,12,18,24,36,48,54]
delftphygofdmxaxis = np.arange(len(delftphygofdmyaxis))
fig6 = plt.figure(6)
plot(delftphygofdmxaxis,delftphygofdmyaxis)
ylabel('Data Rates')
title('Data Rates vs Modulation types for PHY type 802.11g in Delft (Centre) (OFDM)')
#fig6.show ()

delftlistb = []  																	#listt of indexes of PHYB
delftlistphybmcs = [] 																#list of mcs for PHYB
delftlistphybcck = []																#list of cck value for PHYB
delftlistphybofdm = []																#list of ofdm value for PHYB
delftlistphybgfsk = []																#list of gfsk value for PHYB
delftlistphybdynamic = []															#list of dynamic value for PHYB
delftlistphybdatarate = []															#list of datarate for PHYB

for i,j in enumerate(delftlistphy):
	if str(j[0]) == '802.11b':
#		print i
#		delftlistb.append([i])
		delftlistphybmcs.append(delftlistmcs[i])
		delftlistphybcck.append(delftlistcck[i])
		delftlistphybofdm.append(delftlistofdm[i])
		delftlistphybgfsk.append(delftlistgfsk[i])
		delftlistphybdynamic.append(delftlistdynamic[i])
		delftlistphybdatarate.append(delftlistdatarate[i])

#print delftlistphybdatarate
#print delftlistphybofdm

#delftlistphybofdmdatarate = []														#list of ofdm datarates for phyb


delftkhaalilist = []																	#list to check CCk in PHYB

for item in delftlistphybdatarate:
	if str(item[0]) not in delftkhaalilist:
		delftkhaalilist.append(str(item[0]))

#print delftkhaalilist

delftphybcckyaxis = [1,2,5.5,11]
delftphybcckxaxis = np.arange(len(delftphybcckyaxis))
fig7 = plt.figure(7)
plot(delftphybcckxaxis,delftphybcckyaxis)
ylabel('Data Rates')
title('Data Rates vs Modulation types for PHY type 802.11b in Delft (Dorm) (CCK)')
#fig7.show ()

delftlistd = []  																	#listt of indexes of PHYB
delftlistphydmcs = [] 																#list of mcs for PHYB
delftlistphydcck = []																#list of cck value for PHYB
delftlistphydofdm = []																#list of ofdm value for PHYB
delftlistphydgfsk = []																#list of gfsk value for PHYB
delftlistphyddynamic = []															#list of dynamic value for PHYB
delftlistphyddatarate = []															#list of datarate for PHYB

for i,j in enumerate(delftlistphy):
	if str(j[0]) == '802.11 DSSS':
#		print i
#		delftlistb.append([i])
		delftlistphydmcs.append(delftlistmcs[i])
		delftlistphydcck.append(delftlistcck[i])
		delftlistphydofdm.append(delftlistofdm[i])
		delftlistphydgfsk.append(delftlistgfsk[i])
		delftlistphyddynamic.append(delftlistdynamic[i])
		delftlistphyddatarate.append(delftlistdatarate[i])

#print delftlistphybdatarate
#print delftlistphybofdm

#delftlistphybofdmdatarate = []														#list of ofdm datarates for phyb

#print delftlistphyddatarate
delftkhaalilist1 = []																	#list to check CCk in PHYB

for item in delftlistphyddatarate:
	if str(item[0]) not in delftkhaalilist1:
		delftkhaalilist1.append(str(item[0]))

#print delftkhaalilist1
print 'Data Rates for 802.11 DSSS are not available on wireshark'

camplistelementPHY = []																#list of unique elements in listPHY
camplistelementDR = []																#list of unique elements in listdatarate

for item in camplistphy:
	if str(item[0]) not in camplistelementPHY:
		camplistelementPHY.append(str(item[0]))

#print camplistelementPHY

for item in camplistdatarate:
	if str(item[0]) not in camplistelementDR:
		camplistelementDR.append(str(item[0]))

#print camplistelementDR

camplistb = []  																	#listt of indexes of PHYG
camplistphygofdm = []																#list of ofdm value for PHYG
camplistphygcck = []
camplistphyggfsk = []
camplistphygdynamic = []
camplistphygdatarate = []															#list of datarate for PHYG
camplistphygmcs = []

for i,j in enumerate(camplistphy):
	if str(j[0]) == '802.11g':
#		print i
#		camplistb.append([i])
		camplistphygofdm.append(camplistofdm[i])
		camplistphygdatarate.append(camplistdatarate[i])

#print camplistphygofdm
#print camplistphygdatarate

camplistdrphygofdm = []

for i,j in enumerate(camplistphygofdm):
	if str(j[0]) == 'True':
		camplistdrphygofdm.append(camplistphygdatarate[i])

#print camplistdrphygofdm

camplistdrphyg = []

for item in camplistdrphygofdm:
	if str(item[0]) not in camplistdrphyg:
		camplistdrphyg.append(str(item[0]))

#print camplistdrphyg

campphygofdmyaxis = [6,12,24,36,48,54]
campphygofdmxaxis = np.arange(len(campphygofdmyaxis))
fig8 = plt.figure(8)
plot(campphygofdmxaxis,campphygofdmyaxis)
ylabel('Data Rates')
title('Data Rates vs Modulation types for PHY type 802.11g in Delft (Campus) (OFDM)')
#fig8.show ()

camplistb = []  																	#listt of indexes of PHYB
camplistphybmcs = [] 																#list of mcs for PHYB
camplistphybcck = []																#list of cck value for PHYB
camplistphybofdm = []																#list of ofdm value for PHYB
camplistphybgfsk = []																#list of gfsk value for PHYB
camplistphybdynamic = []															#list of dynamic value for PHYB
camplistphybdatarate = []															#list of datarate for PHYB

for i,j in enumerate(camplistphy):
	if str(j[0]) == '802.11b':
#		print i
#		camplistb.append([i])
		camplistphybmcs.append(camplistmcs[i])
		camplistphybcck.append(camplistcck[i])
		camplistphybofdm.append(camplistofdm[i])
		camplistphybgfsk.append(camplistgfsk[i])
		camplistphybdynamic.append(camplistdynamic[i])
		camplistphybdatarate.append(camplistdatarate[i])

#print camplistphybdatarate
#print camplistphybofdm

#camplistphybofdmdatarate = []														#list of ofdm datarates for phyb


campkhaalilist = []																	#list to check CCk in PHYB

for item in camplistphybdatarate:
	if str(item[0]) not in campkhaalilist:
		campkhaalilist.append(str(item[0]))
#print campkhaalilist

campphybcckyaxis = [0,1]
#phybcckxaxis = np.arange(len(phybcckyaxis))
#plt.bar(phybcckxaxis,phybcckyaxis)
#ylabel('Data Rates')
#title('Data Rates vs Modulation types for PHY type 802.11b in Delft (Campus) (CCK)')
#show ()


#drphyb1 = 1																		#PHYB datarate = 1
#drphyb2 = 2																		#PHYB having datarate = 2
#drphyg6 = 6																		#PHYG datarate = 6

#print ('The number of packets with Data Rate = 1 and PHY type 802.11b are: %d ' %drphyb1)
#print ('The number of packets with Data Rate = 1 and PHY type 802.11b are: %d ' %drphyb2)

#avgphybhomedr = 0																#average datarate for PHYB packets in India home

#avgphybhomedr = (drphyb1 + 2*drphyb2)/(drphyb1 + drphyb2)
#print avgphybhomedr

#a = [drphyb1,drphyb2,phybcckyaxis, drphyg6,]															#Plot for Data Rates for PHY type 802.11b in India
#x = np.arange(len(a))
#bar_width = 0.05
#name = ('802.11b CCK India' ,'','802.11b CCK Campus','802.11g OFDM India')
#fig1 = plt.figure(1)
#bar = plt.bar(x,a)
#bar[2].set_color('r')
#bar[3].set_color('y')
#plt.xticks(x + bar_width,name)
#plt.title('Data Rates for PHY type 802.11b and 802.11g')
#plt.ylabel('Data Rate')
#fig1.show()

fig9 = plt.figure(9)
plot(accphygofdmxaxis,accphygofdmyaxis, color = "red", label = "Dorm", linewidth = "2.5")
plot(campphygofdmxaxis,campphygofdmyaxis, color = "green", label = "Campus")
plot(delftphygofdmxaxis,delftphygofdmyaxis, color = "yellow", label = "Centre", )
plot(np.arange(len(drphyg6)), drphyg6, color = "blue", label = "India")
ylabel("Data Rates")
xlabel("Items")
title("Data Rates for 802.11g OFDM")
fig9.legend ()
fig9.show ()

fig10 = plt.figure(10)
plot(delftphybcckxaxis,delftphybcckyaxis, color = "yellow", label = "Centre", linewidth = "2.5")
plot(accphybcckxaxis,accphybcckyaxis, color = "red", label = "Dorm")
plot(np.arange(len(drphyb1)), drphyb1, color = "blue", label = "India")
plot(np.arange(len(campphybcckyaxis)), campphybcckyaxis, color = "green", label = "Campus")
ylabel("Data Rates")
xlabel("Items")
title("Data Rates for 802.11b CCK")
fig10.legend ()
fig10.show ()

raw_input()