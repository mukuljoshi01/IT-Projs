import os
import getpass
import socket
import datetime

#Creating the file which will be having all the required details

file=open('myfinalfile.txt','w')

#Getting the username

username=getpass.getuser()

#Writing the username to the file

file.write(" USERNAME:- " + username  )

#Adding a new line for clarity purposes

file.write("\n \n")

#Fetching the computer name

file.write("COMPUTER NAME : - "+ str(socket.gethostname()) )
file.write("\n \n ")

#Getting the date

date=datetime.date.today()

#Getting the time

time=datetime.datetime.now()

#Using the str function to format the date and time

formated_date=date.strftime(" %d-%m-%Y ")
file.write("Today is " + formated_date)
file.write("\n \n ")

#Formating the time

formated_time=time.strftime("%H: %M(min):%S(seconds)")
file.write("Current time is " + formated_time)
file.write("\n \n ")

#Command used for fetching the total number of processes
total_processes=os.popen("ps aux | wc -l").read()

#Getting the count of the total number of processes running in the system

file.write("TOTAL NUMBER OF PROCESSES RUNNING ON THE SYSTEM ARE :- "  + total_processes)
file.write("\n \n")

#Getting the top 10 processes which are consuming most memory

file.write("---------------LIST OF TOP 10 PROCESSES RUNNING AND CONSUMING MOST MEMORY--------------------- ")
file.write("\n \n")
file.close()


#Appending to the file

os.system("ps aux --sort=-%mem | head >> myfinalfile.txt")




