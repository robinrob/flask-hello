import os
os.chdir('/home/msl/Documents/programming/python/head_first_python/chapter3')
data=open('text.txt')

for line in data:
	print(line.split('i')[0], end='')
