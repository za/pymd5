import sys
import hashlib

f = open('sample_01.wl', 'r')

for line in f:
	list.append(line)

f.close()

print list

# shall I use dictionary or list as data structure? 

#dict={}

# echo the contents

#f = open('sample_01.wl', 'rU')

#for line in f:
#	print line,		
	#dict[line] = 'something'	
	#md5 = hashlib.md5(line)
	#print line,
	#print md5.hexdigest(),
#f.close()

#print dict

#def read_wordlist(filename):
#	"""read the wordlist"""
#	input_file = open(filename, 'r')
#	for line in input_file:
#		print line,
#	input_file.close()
#
#def compute_md5(wordlist):
#	for wordlist in wordlists:
#		hash = hashlib.md5(line)	
#
#def insert_dict():
#
#
#def main():
#	read_wordlist('sample_01.wl')	
#
#if __name__ == '__main__':
#	main()
