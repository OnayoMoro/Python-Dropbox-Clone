#Client code

import socket
import time
from pathlib import Path
from collections import namedtuple
from datetime import datetime

fp = r'Insert windows dir or delete the "r" to use a linux dir format'

#Establish Connection
s = socket.socket()
#Can also used commented code bellow to enter host address via console 
#host = input(str("Please enter server host address: "))
host = "Insert hostname or IP"
port = 420
s.connect((host,port))
print("Connected, file sysnc operational")

#File data structure 
Files = namedtuple('File', 'name path size modified_date')
files1 = [] #Keeps track of destination dir server side
files2 = [] #Keeps track of source dir client side
p = Path(fp)
delay = 1


#Send files
def sendfiles(files):
    print(files)

    #Send request
    request = "add"
    s.send(bytes(request, "utf-8"))
    
    #Send file name and extension
    file_name = files.name
    s.send(bytes(file_name, "utf-8"))
    print("Updating file: ", file_name)

    #Send file object
    namepath = fp + "\\" + file_name
    print(namepath)
    files = open(namepath, 'rb')
    file_data = files.read(204800000)
    print("Data transmitting")
    s.send(file_data)
    time.sleep(delay)


def deletefiles(files):
    print(files)

    #Send request
    request = "delete"
    s.send(bytes(request, "utf-8"))

    #Send file name and extension
    file_name = files.name
    s.send(bytes(file_name, "utf-8"))
    print("Deleting file: ", file_name)
    


def addingfiles():
    for i in range(len(files2)):
        try:
            #If file is on server
            if files2[i].name == files1[i].name:
                
                #If file has not been modified
                if files2[i].modified_date == files1[i].modified_date:
                    print("File ", files2[i].name, " is up to date")
                    
                #If file has been modified
                else:
                    files1[i] = files2[i]
                    sendfiles(files2[i])
                    
            #If file is not on server
            elif files2[i] not in files1:
                files1.insert(i,files2[i])
                sendfiles(files2[i])
        except:
            #If file is not on server
            if files2[i] not in files1:
                files1.insert(i,files2[i])
                sendfiles(files2[i])
            else:
                print("Something went wrong when trying to update files")
        time.sleep(delay)


def deletingfiles():
    i=0
    while (i<len(files1)):
        #If file is deleted on client
        if files1[i] not in files2:
            print("File ", files1[i].name, "deleted")
            deletefiles(files1[i])
            files1.remove(files1[i])
            i-=1
            time.sleep(delay)
                
        #If file is not deleted
        else:
            print("File ", files1[i].name, "not deleted")
            time.sleep(delay)
        i+=1


#Loop through files to populate/initialise base file list
for item in p.glob('**/*'):
    name = item.name
    path = Path.resolve(item).parent
    size = item.stat().st_size
    modified = datetime.fromtimestamp(item.stat().st_mtime)

    #Add file to file list
    files1.append(Files(name, path, size, modified))

    #Send files to server for the first time
    sendfiles(Files(name, path, size, modified))
    time.sleep(delay)


#Loop to constantly re-populate new file list
#and keep the destination dir up to date
while (1==1):

    length = len(files1)

    #Add current files to new file list
    for item in p.glob('**/*'):
        name = item.name
        path = Path.resolve(item).parent
        size = item.stat().st_size
        modified = datetime.fromtimestamp(item.stat().st_mtime)

        #Add file to new file list
        files2.append(Files(name, path, size, modified))

    #Compare lists for changes for ADDING new files to server
    addingfiles()

    #Compare lists for changes for DELETING new files from server
    deletingfiles()
        
    #Clear new file list 
    files2 = []
