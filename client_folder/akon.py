import socket
import sys
import os
import shutil

s = socket.socket()
#host = input(str("Please enter server host address: "))
host = "DESKTOP-MEDSG9I"
port = 420
s.connect((host,port))
print("Connected, file sysnc operational")
 

