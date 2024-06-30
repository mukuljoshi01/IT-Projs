#Importing the socket module
import socket 
soc = socket.socket()

#Making the connection to the windows workstation using the port 5800
soc.connect(("192.168.184.156",5800))

#Specifying that file "myfinalfile.txt" should be opened in the read bytes mode

file_to_be_opened = open("/home/mukuljoshi/myfinalfile.txt", "rb")

#Data is being read into the bytes
file_in_bytes = file_to_be_opened.read(1024)

#Giving the user confirmation that the file is being sent to the workstation
print("File is being sent to the windows workstation")


while (file_in_bytes):
    soc.send(file_in_bytes) 
    file_in_bytes = file_to_be_opened.read(1024)

#Giving the user confirmation that file has been sent successfully    
print("File has been sent successfully")

#Closing the socket
soc.close()

#Priting the final message that Connection has been closed
print("Connection has been  closed.")
