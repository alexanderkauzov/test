#!/bin/python3

num = int(input('Enter num: '))

def armstrong(num):
	summ = 0
	lenght = len(str(num))
	for i in list(str(num)):
		summ += int(i)**lenght
	return summ == num

print(armstrong(num))
