#!/usr/bin/env python3

def getParity(n):
	parity = 0
	while n:
		parity = ~parity
		n = n & (n - 1)
	return parity

def parityimp(binArray):
	res=[]
	for i in binArray:
		if getParity(i):
			b = bin(i)
			b = b[2:]
			res.append("1" + b)
		else:
			b = bin(i)
			b = b[2:]
			res.append("0" + b)
	return res

def paritypair(binArray):
	res=[]
	for i in binArray:
		if getParity(i):
			b = bin(i)
			b = b[2:]
			res.append("0" + b)
		else:
			b = bin(i)
			b = b[2:]
			res.append("1" + b)
	return res
