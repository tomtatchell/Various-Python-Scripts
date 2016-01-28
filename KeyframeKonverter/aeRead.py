from itertools import chain, zip_longest
from PySide import QtGui
import os
import sys

# Fetch data from clipboard
app = QtGui.QApplication(sys.argv)
cb = QtGui.QApplication.clipboard()

# Needs changing to user input / fetch from cb
srcWidth = 1920
srcHeight = 1080

# create temporary file for clipboard data
with open('AEClipboardTemp', 'w+') as tempFile:
    tempFile.write(cb.text())


rotationData = []
scaleData = []
positionData = []


"""
Data Extraction Functions
"""

def extractRotationData():
    keepDataR = False
    with open('AEClipboardTemp', 'r') as aeRead:
        for line in aeRead:
            if line.strip() == "Frame\tdegrees":
                print("rotation data extracted")
                keepDataR = True
            elif line.strip() == "":
                keepDataR = False

            elif keepDataR:
                rotationData.append(line)


def extractScaleData():
    keepDataS = False
    with open('AEClipboardTemp', 'r') as aeRead:
        for line in aeRead:
            if line.strip() == "Frame\tX percent\tY percent\tZ percent" or \
                    line.strip() == "Frame\tX percent\tY percent":
                print("scale data extracted")
                keepDataS = True
            elif line.strip() == "":
                keepDataS = False

            elif keepDataS:
                scaleData.append(line)


def extractPositionData():
    keepDataP = False
    with open('AEClipboardTemp', 'r') as aeRead:
        for line in aeRead:
            if line.strip() == "Frame\tX pixels\tY pixels\tZ pixels" or \
                    line.strip() == "Frame\tX pixels\tY pixels":
                print("transform data extracted")
                keepDataP = True
            elif line.strip() == "":
                keepDataP = False

            elif keepDataP:
                positionData.append(line)

# Column count for nuke keyframe file
nukeCol = 0

# Detect if information exists
with open('AEClipboardTemp', 'r') as aeRead:
    if "degrees" in aeRead.read().strip().split():
        print("rotation data present")
        nukeCol += 1
        extractRotationData()

with open('AEClipboardTemp', 'r') as aeRead:
    if "percent" in aeRead.read().strip().split():
        print("scale data present")
        nukeCol += 2
        extractScaleData()

with open('AEClipboardTemp', 'r') as aeRead:
    if "pixels" in aeRead.read().strip().split():
        print("transform data present")
        nukeCol += 2
        extractPositionData()

print("Nuke columns = ", nukeCol)


"""
Remove redundant data
"""

AERData = []
AESData = []
AEPData = []

# remove frame number
for line in rotationData:
    org = line.strip().split()
    org = org[1::]
    AERData.append(org)

# remove frame number and z coord
for line in scaleData:
    org = line.strip().split()
    with open('AEClipboardTemp', 'r') as aeRead:
        for line in aeRead:
            if line.strip() == "Frame\tX percent\tY percent\tZ percent":
                org = org[1:len(org)-1:]
                AESData.append(org)
            elif line.strip() == "Frame\tX percent\tY percent":
                org = org[1::]
                AESData.append(org)

# remove frame number and z coord
for line in positionData:
    org = line.strip().split()
    with open('AEClipboardTemp', 'r') as aeRead:
        for line in aeRead:
            if line.strip() == "Frame\tX pixels\tY pixels\tZ pixels":
                org = org[1:len(org)-1:]
                AEPData.append(org)
            elif line.strip() == "Frame\tX pixels\tY pixels":
                org = org[1::]
                AEPData.append(org)


"""
Conversions from AE to Nuke data
"""

# Rotation Data Convert
AERData = [(float(x)*(-1)) for line in AERData for x in line]
AERData = [str(line) for line in AERData]
nukeRData = [list(x) for x in zip(AERData)]

# Scale Data Convert
AESData = [(float(x)/100) for line in AESData for x in line]
AESData = [str(line) for line in AESData]
nukeSData = [list(x) for x in zip(AESData[0::2], AESData[1::2])]

# Position Data Convert

# X data
AEPDataX = []
AEPDataX.append(list(coord[0::2] for coord in AEPData))
AEPDataX = [(float(x)-(srcWidth/2))
            for item in AEPDataX for y in item for x in y]
AEPDataX = [str(line) for line in AEPDataX]

# Y data
AEPDataY = []
AEPDataY.append(list(coord[1::2] for coord in AEPData))
AEPDataY = [((srcHeight-(float(x)))-(srcHeight/2))
            for item in AEPDataY for y in item for x in y]
AEPDataY = [str(line) for line in AEPDataY]

# Combine X+Y data
nukePData = [list(x) for x in zip(AEPDataX, AEPDataY)]

# Combine position, rotation and scale data
translationData = [filter(None, col) for col in
                   zip_longest(nukeRData, nukePData, nukeSData)]


"""
Format data for nuke ASCII import
"""

tData = []
for i in translationData:
    for item in i:
        for x in item:
            tData.append(x)

nCB = [tData[x:x+nukeCol] for x in range(0, len(tData), nukeCol)]
nCBFormat = []
for line in nCB:
    nCBFormat.append(line)
    nCBFormat.append("\n")

nCBChain = list(chain.from_iterable(nCBFormat))
nCBChain = " ".join(nCBChain)


"""
Nuke keyframe ASCII File creation functions
"""

def writeToTemp():
    with open("nukeKeysTemp.txt", 'w') as keyFile:
        keyFile.write(str(nCBChain))


def nukeKeysCreate():
    with open("nukeKeysOut_v01.txt", 'w') as writeOut:
        with open("nukeKeysTemp.txt", 'r') as wSFix:
            for line in wSFix:
                cleanLine = line.lstrip()
                writeOut.write(cleanLine)


def nukeKeysTempDel():
    os.remove("nukeKeysTemp.txt")

def cleanUp():
    try:
        os.remove("AEClipboardTemp")
    except OSError:
        pass


writeToTemp()
nukeKeysCreate()
nukeKeysTempDel()
cleanUp()