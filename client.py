import socket
import time
from pathlib import Path
from collections import namedtuple
from datetime import datetime

fp = r'Insert windows dir or delete the "r" to use a linux dir format'

#Establish Connection
s = socket.socket()
#host = input(str("Please enter server host address: "))
host = "DESKTOP-MEDSG9I"
port = 420
s.connect((host,port))
print("Connected, file sysnc operational")

#File data structure 
Files = namedtuple('File', 'name path size modified_date')
files1 = [] #Keeps track of source dir server side
files2 = [] #Keeps track of source dir client side
p = Path(fp)
c = 0

#Send files
def sendfiles(files):
    print(files)
    
    #Send file name and extension
    file_name = files.name
    s.send(bytes(file_name, "utf-8"))
    print("Updating file: ", file_name)

    #Send file object
    namepath = fp + "\\" + file_name
    print(namepath)
    files = open(namepath, 'rb')
    file_data = files.read(2048)
    print("Data transmitting")
    s.send(file_data)


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
    time.sleep(2)

#Loop to constantly re-populate new file list 
while (1==1):

    #Add current files to new file list
    for item in p.glob('**/*'):
        name = item.name
        path = Path.resolve(item).parent
        size = item.stat().st_size
        modified = datetime.fromtimestamp(item.stat().st_mtime)


        #Add file to new file list
        files2.append(Files(name, path, size, modified))

    #Compare lists for changes for ADDING new files to server
    for i in range(len(files2)):
        try:
            if files2[i] in files1:
                print("File ", files2[i].name, " is up to date")
            elif files2[i] not in files1:
                files1.append(files2[i])
                sendfiles(files2[i])
        except:
            print("Something went wrong")
        time.sleep(2)

    #Compare lists for changes for DELETING new files from server

    #Clear new file list 
    files2 = []
                


    
    



    
    




#If changes detected, send files to server

