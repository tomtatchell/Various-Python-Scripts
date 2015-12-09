nukeRead = open("/Users/bbmp03/Desktop/temp/KeyframeKonverter/NukeOut.txt",'r+')

nukeValues = []

for line in nukeRead:
    nukeValues.append([float(n) for n in line.strip().split(' ')])



nukeFrames = []
nukeRot = []
nukeSW = []
nukeSH = []
nukeTX = []
nukeTY = []

for value in nukeValues:
    nukeFrames.append(nukeValues.index(value))
    try:
        r, sW, sH, tX, tY = value[0], value[1], value[2], value[3], value[4]

        print ("Frame = ", nukeValues.index(value))
        print ("Rotation = ",  r)
        nukeRot.append(r)
        print ("Scale Width = ", sW)
        nukeSW.append(sW)
        print ("Scale Height = ", sH)
        nukeSH.append(sH)
        print ("Translate X = ", tX)
        nukeTX.append(tX)
        print ("Translate Y = ", tY)
        nukeTY.append(tY)
    except IndexError:
        print("A line in the file doesn't have enough entries.")

print("TEST")
print("nukeFrames = ", nukeFrames)
print("nukeRot = ", nukeRot)
print("nukeSW = ", nukeSW)
print("nukeSH = ", nukeSH)
print("nukeTX = ", nukeTX)
print("nukeTY = ", nukeTY)