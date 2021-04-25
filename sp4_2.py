import hashlib
import sys
import os

def hash_file():
	filename=input("File name: ")
	with open(filename, 'rb') as file:
		data = file.read()
		n= hashlib.md5(data).hexdigest()
	print ('Hash file: ')
	print(n) + Fork()

def Fork():
	read=None
	while True:
		read = input("Continue? [y/n]")
		if read == "y":
			fork_nev = os.fork()
			if fork_nev ==0:
				print('PID of the child process: {}'.format(os.getpid()))
				hash_file()
			else:
				print('PID of the parent process: {}'.format(os.getpid()))
				os.wait()
		if read == "n":
			os._exit(0)

Fork()
