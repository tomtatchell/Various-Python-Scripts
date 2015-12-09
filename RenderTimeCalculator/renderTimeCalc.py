#user input

def getTime():
    fTimeMin = input("Mins per frame: ")
    fTimeSec = input("Sec per frame: ")
    fTime = (int(fTimeMin)*60) + int(fTimeSec)
    #print ("time in sec = ", fTime)
    return fTime

def getFrames():

    renderFrames = int(input("Number of frames to render: "))
    print ("frames to render = ", renderFrames)
    return renderFrames

def calc(time, frames):
    totalTime = int(time) * int(frames)
    totalSec = totalTime
    totalMins = totalSec / 60
    totalHrs = totalMins / 60

    print ("Total sec: %s\nTotal Mins: %s\nTotal Hrs: %s" % (int(totalSec), int(totalMins), int(totalHrs)))

    if totalMins > 60:
        print ("Time Remaining: %2i Hour(s) : %2i Min(s) : %2i Second(s)" % (int(totalHrs), (int(totalMins) - (int(totalHrs)*60)), int(totalSec) - (int(totalMins)*60)))
    else:
        print ("Such time!")
        print ("Time Remaining: %2i Min(s) : %2i Second(s)" % (int(totalMins), (int(totalSec) - (int(totalMins)*60))))





calc(getTime(), getFrames())