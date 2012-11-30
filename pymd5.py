import hashlib

#dict={}

# echo the contents

f = open('sample_01.wl', 'rU')

for line in f:
	print line,		
	#dict[line] = 'something'	
	#md5 = hashlib.md5(line)
	#print line,
	#print md5.hexdigest(),
f.close()

#print dict
