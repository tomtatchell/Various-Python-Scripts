from PySide import QtGui
import sys



app = QtGui.QApplication(sys.argv)
cb = QtGui.QApplication.clipboard()

tempfile = open("temp.txt", "w+")
tempfile.write(cb.text())



"""

"""
#Open File
"""
keyFile = open("AEKeyframeFile.txt", "w")


"""
#AE Header Data
"""
fps = 25
srcWidth = 1920
srcHeight = 1080

aeHeader = ["Adobe After Effects 8.0 Keyframe Data\n\n",
          "\tUnits Per Second\t", str(fps), "\n",
          "\tSource Width\t", str(srcWidth), "\n",
          "\tSource Height\t", str(srcHeight), "\n",
          "\tSource Pixel Aspect Ratio\t1\n",
          "\tComp Pixel Aspect Ratio\t1\n\n"]

for line in aeHeader:
    keyFile.write(line)


"""
#Get data from nuke ASCII file
"""
nukeRead = open("/Users/bbmp03/Desktop/temp/KeyframeKonverter/\
NukeOut_test01.txt",'r+')

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
        nukeRot.append(r)
        nukeSW.append(sW)
        nukeSH.append(sH)
        nukeTX.append(tX)
        nukeTY.append(tY)
        nukeRead.close()
    except IndexError:
        print("A line in the file doesn't have enough entries.")
        nukeRead.close()

"""
#Nuke to AE Conversions
"""
#rotation conversion
nToAERot = []
for nValue in nukeRot:
    nToAERot.append(nValue * (-1))

#translation conversion
nToAETY = []
for nValue in nukeTY:
    nToAETY.append((srcHeight-nValue)-(srcHeight*0.5))

nToAETX = []
for nValue in nukeTX:
    nToAETX.append((nValue)+(srcWidth*0.5))

#scale conversions
nToAESW = []
for nValue in nukeSW:
    nToAESW.append(nValue*100)

nToAESH = []
for nValue in nukeSH:
    nToAESH.append(nValue*100)


"""
#Transform Rotation
"""

def transRotHeader():

    transRotText = ["Transform\tRotation\n",
                    "\tFrame\tdegrees\n"]

    for line in transRotText:
        keyFile.write(line)

def transRot(nukeFrames, nToAERot):

    transRotData = []
    count = 0

    for x in nToAERot:

        transRotData.append("\t")
        transRotData.append(nukeFrames.index(count))
        count += 1
        transRotData.append("\t")
        transRotData.append("%.5f" % x)
        transRotData.append("\n")
    #return (transRotData)
    transRotData.append("\n")
    for line in transRotData:
        #print(line)
        keyFile.write(str(line))

transRotHeader()
transRot(nukeFrames, nToAERot)

"""
#Transform Scale
"""

def transScaleHeader():

    transScaleText = ["Transform\tScale\n",
                    "\tFrame\tX percent\tY percent\tZ percent\n"]

    for line in transScaleText:
        keyFile.write(line)

def transScale(nukeFrames, scaleX, scaleY):

    transScaleData = []
    count = 0
    scaleZip = list(zip(scaleX, scaleY))

    for x in scaleZip:

        transScaleData.append("\t")
        transScaleData.append(nukeFrames.index(count))
        count += 1
        transScaleData.append("\t")
        transScaleData.append("%.3f" % x[0])
        transScaleData.append("\t")
        transScaleData.append("%.3f" % x[1])
        transScaleData.append("\t")
        transScaleData.append(100)
        transScaleData.append("\n")

    transScaleData.append("\n")
    for line in transScaleData:
        keyFile.write(str(line))



transScaleHeader()
transScale(nukeFrames, nToAESW, nToAESH)

"""
#Transform Position
"""

def transPosHeader():

    transPosText = ["Transform\tPosition\n",
                    "\tFrame\tX pixels\tY pixels\tZ pixels\n"]

    for line in transPosText:
        keyFile.write(line)

def transPosition(nukeFrames, tX, tY):

    transPosData = []
    count = 0
    positionZip = list(zip(tX, tY))

    for x in positionZip:
        transPosData.append("\t")
        transPosData.append(nukeFrames.index(count))
        count += 1
        transPosData.append("\t")
        transPosData.append("%.3f" % x[0])
        transPosData.append("\t")
        transPosData.append("%.3f" % x[1])
        transPosData.append("\t")
        transPosData.append(0)
        transPosData.append("\n")

    transPosData.append("\n")
    for line in transPosData:
        keyFile.write(str(line))


transPosHeader()
transPosition(nukeFrames, nToAETX, nToAETY)


endText = "\nEnd of Keyframe Data"
keyFile.write(endText)


keyFile.close()

"""