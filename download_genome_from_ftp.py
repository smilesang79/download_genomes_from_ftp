#!/usr/bin/env python

import sys, getopt

def main(argv):
	ftpfile = ''
	try:
		opts, args = getopt.getopt(argv,"hh:f:",["help", "ftp="]) #"=" means that something is needed as argument
	except getopt.GetoptError:
		print(sys.argv[0], "--ftp <ftpcsvfile>") # py file name
		sys.exit(2)
	for opt, arg in opts:
		if (opt == "-h") or (opt == "--help"):
			print("--ftp: csv file containing ftp addresses of genomes")
			print("-f: csv file containing ftp addresses of genomes/ file name auto-completion not working")
			sys.exit() # -h and --help both working fine
		elif opt in ("-f", "--ftp"):
			ftpfile = arg # argument should be present
			print("Genome ftp csv file is", ftpfile) # -f and --ftp both working/ --ftp --> auto-completion of a file name

if __name__ == "__main__":
	main(sys.argv[1:])
# add commandline arguments

def create_list_from_csv (file):
	import csv
	with open(file, newline='') as f:
		reader = csv.reader(f)
		data = list(reader) # list of a list
	#return data
	#return data[0]
	return [i[1] for i in data] # csv file containing multiple lines
# create a function to read a list from a csv file

def download_genbank_file(ftp):
	import wget
	url = ftp + "/" + ftp.split("/")[-1] + "_genomic.fna.gz"
	wget.download(url) 
# create a function to download a genbank file

#import sys
#ftpFile = sys.argv[1]  #ftp file name is the first commandline argument/ now --ftp	
ftpFile = sys.argv[2]
#ftpFile = "ftp.csv" 
ftpList = create_list_from_csv(ftpFile) # creat a list from ftp file 

for ftp in ftpList:	
	download_genbank_file(ftp) 
	print(ftp, "genome created") # show the progress
# download genbank files with a loop 

#def show_file_list():
#	import os
#	arr = os.listdir()
#	print(arr)	 #selected
#show_file_list() 
# check the list of files in the current directory
