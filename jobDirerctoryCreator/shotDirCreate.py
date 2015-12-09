import os
from tkinter import *

master = Tk()
master.title("Shot Folders")

l = Label(master, text="Number of shot folders to create:")
l.pack()

e = Entry(master, justify='center')
e.pack()
e.focus_set()


def folderCreation(shots):
    for x in range(1, shots + 1):
        folderName = "shot%02d" % x

        assets = "/%02d-assets" % x
        exports = "/%02d-exports" % x
        fs = "/%02d-fs" % x
        ref = "/%02d-ref" % x
        renders = "/%02d-renders" % x

        comp = "/%02d-comp" % x
        ae = "/%02d-ae" % x
        nuke = "/%02d-nuke" % x

        models = "/%02d-models" % x
        tex = "tex"

        output = "/%02d-output" % x
        sequence = "/%02d-sequence" % x
        wips = "/%02d-wips" % x

        source = "/%02d-source" % x
        # Sequence Folder
        footage = "/%02d-footage" % x
        stills = "/%02d-stills" % x


        os.makedirs(folderName + assets + exports)
        os.makedirs(folderName + assets + fs)
        os.makedirs(folderName + assets + ref)
        os.makedirs(folderName + assets + renders)
        os.makedirs(folderName + comp + ae)
        os.makedirs(folderName + comp + nuke)
        os.makedirs(folderName + models + "/tex")
        os.makedirs(folderName + output + sequence)
        os.makedirs(folderName + output + wips)
        os.makedirs(folderName + source + footage)
        os.makedirs(folderName + source + sequence)
        os.makedirs(folderName + source + stills)

def callback():
    shotNumber = e.get()
    print (shotNumber)
    folderCreation(int(shotNumber))
    master.quit()

b1 = Button(master, text="Submit", command=callback)
b1.pack()

mainloop()