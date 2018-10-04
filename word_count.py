#!/usr/bin/env python

import argparse


parser = argparse.ArgumentParser( description="" )

parser.add_argument(
	"data_file",   #name the file
	help="path to the file we want to read"  #descreption of the file
)

#-------------------------------------------------------------------------------
# Are there other arguments we need? NO!!!
#-------------------------------------------------------------------------------

args = parser.parse_args( )
#how would you check the file that the script is doing what you expected
print(args.data_file)

fh = open(args.data_file)
print ("the file handle is", fh)

lines = 0
words = 0
chars = 0

#read the filw line by line
for line in fh:
	print(line)
	

#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
