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

#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
