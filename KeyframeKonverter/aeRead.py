keyFile = open("nukeKeys_test_v01.txt", 'w')
keepData = False

rotationData = []
scaleData = []
positionData = []
def extractRotationData():
    keepData = False
    with open('/Users/bbmp03/GitHub/Various Python Scripts/KeyframeKonverter/dataFiles/clipboard Data/AEOut.txt', 'r') as aeRead:
        for line in aeRead:
            if line.strip() == ("Frame\tX percent\tY percent\tZ percent"):
                keepData = True
            elif line.strip() == (""):
                keepData = False

            elif keepData:
                #keyFile.write(line)
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
                #keyFile.write(line)
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
                #keyFile.write(line)
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


#print(rotationData)

print ("Rotation Data")
for line in rotationData:
    print (line.strip().split())

print ("Scale Data")
for line in scaleData:
    print (line.strip().split())

print ("Position Data")
for line in positionData:
    print (line.strip().split())



keyFile.close()