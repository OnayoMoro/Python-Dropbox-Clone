import socket

s = socket.socket()
host = socket.gethostname()
port = 420
s.bind((host,port))
print("Server host name: " + host)
s.listen(1)
print("Waiting for client request...")
conn, addr = s.accept()
print(addr, "has successfully connected to the server")

while (1==1):
    
    
    
    
    file_name = conn.recv(1024)
    print(file_name)
    print("Updating file: ", file_name.decode("utf-8"))
    file_data = conn.recv(2048)
    file = open(file_name.decode("utf-8"), 'wb')
    file.write(file_data)
    file.close()
    print("File recieved")
    #break

    


