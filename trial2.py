#!/usr/bin/python

import hashlib

f = open('sample_01.wl', 'r')

print "Name of the wordlist is ", f.name

li = f.readlines()
#print "The wordlist: %s" % (li)
print li

for l in li: 
	md5 = hashlib.md5(l)
	print md5.hexdigest(), l,

f.close()
