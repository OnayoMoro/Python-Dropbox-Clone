#Server code

import socket
import os

#Create server a
s = socket.socket()
host = socket.gethostname()
port = 420
s.bind((host,port))
print("Server host name: " + host)
#Listen for 1 client
s.listen(1)
print("Waiting for client request...")
#Connect to client
conn, addr = s.accept()
print(addr, "has successfully connected to the server")
#Destination path
fp = r'Insert windows dir or delete the "r" to use a linux dir format'

#Add/update file request
def addfile():
    #Recieve name of file
    file_name = conn.recv(204800000).decode("utf-8")
    #Name of file attatched to destination dir
    namepath = fp + "\\" + file_name
    print("Updating file: ", file_name)
    #Revive files
    file_data = conn.recv(204800000)
    #Create file in destination dir
    file = open(namepath, 'wb')
    file.write(file_data)
    file.close()
    print("File recieved")

def deletefile():
    print("Deletefile method hit")
    #Recieve name of file 
    file_name = conn.recv(204800000).decode("utf-8")
    #Name of file attached to destination dir
    namepath = fp + "\\" + file_name
    print("Deleting file: ", file_name)
    #Delete file 
    os.remove(namepath)
    print("File deleted")

while (1==1):
    
    try:
        print("Waiting for client request...")
        #Recieve request
        request = conn.recv(2048).decode("utf-8")
        print(request)
        #Add/update file request
        if (request ==  "add"):
            addfile()
        #Delete file request
        elif(request == "delete"):
            deletefile()
        
    except:
        conn, addr = s.accept()

    


