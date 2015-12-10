from itertools import chain
import os

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

def nukeKeysTempDel():
    os.remove("nukeKeysTemp.txt")

writeToTemp()
nukeKeysCreate()
nukeKeysTempDel()