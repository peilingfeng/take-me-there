#!/usr/bin/env python2
N=int(input("input number:"))

i=0
while i<=N:
	print(i),
	if (i%3==0):
		print ("Fuzz"),
	if i%5==0:
		print ("Buzz"),
	print (" ")
	i=i+1
	
