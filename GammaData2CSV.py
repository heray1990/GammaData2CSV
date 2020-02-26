#!/usr/bin/python

import sys
import os

def traverse_files(filePath):
    pathDir = os.listdir(filePath)
    for subfolder in pathDir:
        newDir = os.path.join(filePath, subfolder)
        if os.path.isfile(newDir):
            if os.path.splitext(newDir)[1]==".txt":
                if os.path.splitext(newDir)[0][-19:]=="Normal_AdjGammaData":
                    print("hello world")
                else:
                    pass
        else:
            traverse_files(newDir)

def main():
    traverse_files(sys.argv[1])

if __name__=='__main__':
    main()