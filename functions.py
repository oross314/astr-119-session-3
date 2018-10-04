#!/usr/bin/env python3
import numpy as np
import sys

#define a function that returns a value
def expo(x):
	return np.exp(x)		#return np e^x
	
#Define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):	
		print(expo(float(i)))
		
#Define a main function
def main():
	n=10  #provide a default function for n
	
	#check if there is a command line argument provided
	if(len(sys.argv)>1):
		n=int(sys.argv[1]) 		#if argument was provided, use it for n
		
	show_expo(n)		#call the show_expo subroutine
	
#run the main function
if __name__ == "__main__":
	main()