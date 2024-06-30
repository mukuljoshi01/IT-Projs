#Importing the scoket module
import socket
soc=socket.socket()

#Binding the socket to the port 5800
soc.bind(("192.168.184.156",5800))
soc.listen(5)

#Printing to terminal that "Connection is being made"
print("Connection is in progress ")

#Accepting the connection which is being made by the socket

conn ,addr=soc.accept()

#Opening the file( Finalfile.txt) in wb (write bytes) mode which will be having the data which is being transfered

newfile=open("FinalFile.txt","wb")

#Giving the confirmation to the user that connection has been successfuly established

print("Connection has been successfully established")

#Setting up loop for constantly reading the bytes from the file and recieving it over from the python workstation

while True:
    print("Data is being collected")
    data_transfered=conn.recv(1024) #bytes

#If data is available in the file a new file named (FinalFile.txt) will be created  
    if data_transfered:
     newfile.write(data_transfered)
     
#If there is nothing in the file the loop will break and code will exit     
    else:
        break
    
#Closing the socket

soc.close()

#Closing the file 

newfile.close()

#Giving the confirmation that file has been succesfully transferred and the file is created on the desktop

print(" Connection has been successfully Closed")
print(" File has been created on the desktop. It is having the data which is transferred ")
print(" Thanks for using the script and have a nice day  ")
