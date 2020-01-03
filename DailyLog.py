#!/usr/bin/python3

# imports
from datetime import datetime

# Build header components
header = "## Daily Work Log"
name = "Noel Kelly"
company = "RapidProtoInc"
#date = "02/01/2020"
date = str(datetime.date(datetime.now()))
nameFull = "## Engineer: " + name
companyFull = "## Company: " + company
dateFull = "## Date: " + date
textList = [header, nameFull, companyFull, dateFull]
logfilename = "Log_"+date[0:4]+date[5:7]+date[8:10]+".txt"
exit_command = "X"

# Write header to file
#check if file exists:
try:
	with open(logfilename) as outF:
		file_exists = 1
		outF.close
except FileNotFoundError:
	file_exists = 0

# if new file, add header:
if file_exists==0:
	with open(logfilename, "w") as outF:
		for line in textList:
			# write line to output file
			outF.write(line)
			outF.write("\n")

# Wait for journal entries (how to do this?)
with open(logfilename, "a") as outF:
	outF.write("\n")
	exit_flag=0
	while exit_flag == 0:
		#capture user input
		data_str = input("Next Entry: ")
		clear_str = "\033[A"
		for i in range(len(data_str)+12):
			clear_str = clear_str + " "
		clear_str = clear_str + "\033[A"
		print(clear_str)
		#check for exit command (X)
		if data_str == exit_command:
			exit_flag=1
		else:
			#print to file
			time_str = str(datetime.time(datetime.now()))
			entryFull = time_str[0:5]+" : "+data_str 	
			outF.write(entryFull+"\n")
			#print to screen
			print((entryFull))

# Get out
print("Done!")
