#!/usr/bin/python

import sys
import os
import csv

OUT_CSV_FILE = "out.csv"
OUT_CSV_FILE_COOL = "cool.csv"
OUT_CSV_FILE_NORMAL = "normal.csv"
OUT_CSV_FILE_WARM = "warm.csv"

def txt_to_csv(filePath, outPath, colorTemp, datatype, sn):
    fin = open(filePath,'rU')
    row = []
    row.append(colorTemp)
    row.append(sn)
    for line in fin:
        if line.strip().split(" ")[0] not in ["", "x"]:
            if datatype == "-gm":
                row.append(line.strip().split(" ")[3])
            elif datatype == "-xy":
                print(line.strip().split(" ")[0:2])

    print(row)
    fin.close()

    with open(outPath, "a+", newline='') as f:
        fcsv = csv.writer(f)
        fcsv.writerow(row)

def traverse_files(filePath, outPath, colorTemp, datatype):
    pathDir = os.listdir(filePath)

    for subfolder in pathDir:
        newDir = os.path.join(filePath, subfolder)
        if os.path.isfile(newDir):
            if os.path.splitext(newDir)[1] == ".txt":
                if colorTemp == "-c":
                    if os.path.splitext(newDir)[0][-17:]=="Cool_AdjGammaData":
                        sn = os.path.splitext(newDir)[0].split(os.sep)[-1][:-17]
                        txt_to_csv(newDir, outPath, "Cool", datatype, sn)
                    else:
                        pass
                elif colorTemp == "-n":
                    if os.path.splitext(newDir)[0][-19:]=="Normal_AdjGammaData":
                        sn = os.path.splitext(newDir)[0].split(os.sep)[-1][:-19]
                        txt_to_csv(newDir, outPath, "Normal", datatype, sn)
                    else:
                        pass
                elif colorTemp == "-w":
                    if os.path.splitext(newDir)[0][-17:]=="Warm_AdjGammaData":
                        sn = os.path.splitext(newDir)[0].split(os.sep)[-1][:-17]
                        txt_to_csv(newDir, outPath, "Warm", datatype, sn)
                    else:
                        pass
                elif colorTemp == "-o":
                    if os.path.splitext(newDir)[0][-14:]=="_OrigGammaData":
                        sn = os.path.splitext(newDir)[0].split("/")[-1][:-14]
                        txt_to_csv(newDir, outPath, "Origin", datatype, sn)
                    else:
                        pass
        else:
            traverse_files(newDir, outPath, colorTemp, datatype)

def main():
    if len(sys.argv) != 4:
        print("usage: python3 GammaData2CSV.py path -colorTemp(-c:cool -n:normal -w:warm -o:origin) -datatype(-gm:gamma -xy:color coordinate).")
        sys.exit(1)

    match = [parameter for parameter in ["-c", "-n", "-w", "-o"] if sys.argv[2] in parameter]
    if match:
        if sys.argv[2] == "-c":
            outPath = os.path.join(sys.argv[1], OUT_CSV_FILE_COOL)
        elif sys.argv[2] == "-n":
            outPath = os.path.join(sys.argv[1], OUT_CSV_FILE_NORMAL)
        elif sys.argv[2] == "-w":
            outPath = os.path.join(sys.argv[1], OUT_CSV_FILE_WARM)
        else:
            outPath = os.path.join(sys.argv[1], OUT_CSV_FILE)
        if os.path.isfile(outPath):
            os.remove(outPath)

        traverse_files(sys.argv[1], outPath, sys.argv[2], sys.argv[3])
    else:
        print("Please enter a correct colorTemp type.\n-c:cool -n:normal -w:warm -o:origin")

if __name__=='__main__':
    main()