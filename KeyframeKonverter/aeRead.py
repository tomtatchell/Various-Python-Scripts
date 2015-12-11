from itertools import chain
import os

srcWidth = 1920
srcHeight = 1080


keepData = False

rotationData = []
scaleData = []
positionData = []
def extractRotationData():
    keepData = False
    with open('/Users/bbmp03/GitHub/Various Python Scripts/KeyframeKonverter/dataFiles/clipboard Data/AEOut.txt', 'r') as aeRead:
        for line in aeRead:
            if line.strip() == ("Frame\tdegrees"):
                keepData = True
            elif line.strip() == (""):
                keepData = False

            elif keepData:
                rotationData.append(line)

def extractScaleData():
    keepData = False
    with open('/Users/bbmp03/GitHub/Various Python Scripts/KeyframeKonverter/dataFiles/clipboard Data/AEOut.txt', 'r') as aeRead:
        for line in aeRead:
            if line.strip() == ("Frame\tX percent\tY percent\tZ percent"):
                keepData = True
            elif line.strip() == (""):
                keepData = False

            elif keepData:
                scaleData.append(line)

def extractPositionData():
    keepData = False
    with open('/Users/bbmp03/GitHub/Various Python Scripts/KeyframeKonverter/dataFiles/clipboard Data/AEOut.txt', 'r') as aeRead:
        for line in aeRead:
            if line.strip() == ("Frame\tX pixels\tY pixels\tZ pixels"):
                keepData = True
            elif line.strip() == (""):
                keepData = False

            elif keepData:
                positionData.append(line)



with open('/Users/bbmp03/GitHub/Various Python Scripts/KeyframeKonverter/dataFiles/clipboard Data/AEOut.txt', 'r') as aeRead:
    if "Rotation" in aeRead.read().strip().split():
        extractRotationData()

with open('/Users/bbmp03/GitHub/Various Python Scripts/KeyframeKonverter/dataFiles/clipboard Data/AEOut.txt', 'r') as aeRead:
    if "Scale" in aeRead.read().strip().split():
        extractScaleData()

with open('/Users/bbmp03/GitHub/Various Python Scripts/KeyframeKonverter/dataFiles/clipboard Data/AEOut.txt', 'r') as aeRead:
    if "Position" in aeRead.read().strip().split():
        extractPositionData()


AERData = []
AESData = []
AEPData = []

for line in rotationData:
    org = line.strip().split()
    #remove frame number
    org = org[1::]
    AERData.append(org)

for line in scaleData:
    org = line.strip().split()
    #remove frame number + z coord
    org = org[1:len(org)-1:]
    AESData.append(org)

for line in positionData:
    org = line.strip().split()
    #remove frame number + z coord
    org = org[1:len(org)-1:]
    AEPData.append(org)

"""
Conversions:
"""

#Rotation Data Convert
AERData = [(float(x)*(-1)) for line in AERData for x in line]
AERData = [str(line) for line in AERData]
AERData = [list(x) for x in zip(AERData)]
print("AERDATA = ",AERData)

#Scale Data Convert
AESData = [(float(x)/100) for line in AESData for x in line]
AESData = [str(line) for line in AESData]
AESData = [list(x) for x in zip(AESData[0::2],AESData[1::2])]
print("ARSDATA = ", AESData)

#Position Data Convert
AEPDataX = []
AEPDataX.append(list(coord[0::2] for coord in AEPData))
print("AEPDATAX = ", AEPDataX)
AEPDataX = [(((float(x)*(-1))+srcHeight)) for item in AEPDataX for y in item for x in y]
AEPDataX = [str(line) for line in AEPDataX]
print("AEPDATAX CONV = ", AEPDataX)


AEPDataY = []
AEPDataY.append(list(coord[1::2] for coord in AEPData))
print("AEPDATAY = ", AEPDataY)
AEPDataY = [(((float(x)*(-1))+srcHeight)) for item in AEPDataY for y in item for x in y]
AEPDataY = [str(line) for line in AEPDataY]
print("AEPDATAY CONV = ", AEPDataY)

AEPData = [list(x) for x in zip(AEPDataX, AEPDataY)]
print ("AEPDATA = ", AEPData)




translationData = zip(AERData, AESData, AEPData)
translationData = list(translationData)

tData = []
for i in translationData:
    for item in i:
        for x in item:
            tData.append(x)

nCB = [tData[x:x+5] for x in range(0, len(tData), 5)]
#print("nCB: ", nCB)
nCBFormat = []
for line in nCB:
    nCBFormat.append(line)
    nCBFormat.append("\n")

nCBChain = list(chain.from_iterable(nCBFormat))
#print("nCBChain: ",nCBChain)
nCBChain = " ".join(nCBChain)

def writeToTemp():
    with open("nukeKeysTemp.txt", 'w') as keyFile:
        keyFile.write(str(nCBChain))

def nukeKeysCreate():
    with open("nukeKeysOut_v01.txt", 'w') as writeOut:
        with open("nukeKeysTemp.txt", 'r') as wSFix:
            for line in wSFix:
                cleanline = line.lstrip()
                writeOut.write(cleanline)
                #print("Result: ", cleanline)

def nukeKeysTempDel():
    os.remove("nukeKeysTemp.txt")

writeToTemp()
nukeKeysCreate()
nukeKeysTempDel()