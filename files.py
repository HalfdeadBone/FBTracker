import os
import csv
from MsgHandling import *

def CreateDIR(path):
    try:
        if not os.path.isdir(path):
            os.makedirs(path) 
    except Exception as e:
        print(ErrorMsg("Unexpected", str(e)))

def CreateUserDIR(path,name):
    fullPath = os.path.join(path,name)
    try: 
        if not os.path.isdir(fullPath) :
            os.makedirs(fullPath) 
    except Exception as e:
        print(ErrorMsg("Unexpected", str(e)))   
    return fullPath

def CreateJSON(path, name, id_fb):
    fileName = name + '.json'
    try: 
        fullPath=os.path.join(path,name,fileName)
        if not os.path.isfile(fullPath):
            with open(fullPath, 'w') as some:

                print(InfoMsg(fileName, "File Has been Created"))
        else:
            pass
    except Exception as e:
        print(ErrorMsg("Unexpected Error Has Occured", str(e)))


def NewAppendCSV(path,date,valDict):
    fileName = date + '.csv'
    try:
        fullPath=os.path.join(path,valDict['name'],fileName)
        if os.path.isfile(fullPath):
            with open(fullPath, 'a+') as f:
                csvApp = csv.writer(f)
                csvApp.writerow(valDict.values())
        else:
            CreateUserDIR(path,valDict['name'])
            with open(fullPath, 'a+') as f:
                csvApp = csv.writer(f)
                csvApp.writerow(valDict.keys())
                csvApp.writerow(valDict.values())
    
    except Exception as e:
        print(ErrorMsg("Unexpected Error Has Occured", str(e)))

def ReadCSV(path):
    users = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            users.append(row)
    return users

def CreateCSV(path,name,dumpList):
    if dumpList:
        fileName = name + '.csv'
        fullPath = os.path.join(path,fileName)
        with open(fullPath,'w+', encoding='utf8', newline='') as f:
            csvApp = csv.DictWriter(f,fieldnames=dumpList[0].keys())
            csvApp.writeheader()
            csvApp.writerows(dumpList)

def DeleteFile(path, fileName):
    f = os.path.join(path,fileName)
    if os.path.isfile(f):
        os.remove(f)