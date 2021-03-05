#Server code

import socket
import os

s = socket.socket()
host = socket.gethostname()
port = 420
s.bind((host,port))
print("Server host name: " + host)
s.listen(1)
print("Waiting for client request...")
conn, addr = s.accept()
print(addr, "has successfully connected to the server")

def addfile():
    file_name = conn.recv(204800000).decode("utf-8")
    print("Updating file: ", file_name)
    file_data = conn.recv(204800000)
    file = open(file_name, 'wb')
    file.write(file_data)
    file.close()
    print("File recieved")

def deletefile():
    print("Deletefile method hit")
    file_name = conn.recv(204800000).decode("utf-8")
    print("Deleting file: ", file_name)
    os.remove(file_name)
    print("File deleted")

while (1==1):
    
    try:
        print("Waiting for client request...")
        request = conn.recv(2048).decode("utf-8")
        print(request)
        if (request ==  "add"):
            addfile()
        elif(request == "delete"):
            deletefile()
        
        
        
    except:
        conn, addr = s.accept()

    


