import os

BASE_DIR = "c:/windows/system32"
for crrentFolder,subfolders,fileNmaes in os.walk(BASE_DIR):
    print(crrentFolder)
    print(subfolders)
    for f in fileNmaes:
        print('fileNmaes...',f)