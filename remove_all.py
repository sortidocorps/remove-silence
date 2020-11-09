#!/usr/bin/python
import glob
import sys
import os

argv =sys.argv

"""> python remove_all.py "C:/temp" "*" "mp4" """
if len(argv)==4:
    try:

        print("** Start ")
        path = argv[1]
        """ * """
        discriminent = argv[2]
        """ mp4 """
        extention = argv[3] 

        fullPath = path + "/" + discriminent + "." + extention
        print(fullPath)

        filesNames = [os.path.basename(x) for x in glob.glob(fullPath)]


        for name in filesNames:
            try:
                print('auto-editor '+ path+"/"+name)
                os.system('auto-editor '+path+"/"+name +" --no_open")
            except:
                print("Error on auto-editor generate")
                exit(1)


        print("** End ")
        exit(0)
    except:
        print("Error on file")
        exit(1)

