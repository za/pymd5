#!/usr/bin/python

import hashlib

f = open('sample_01.wl','rU')

wordlist = [l.strip() for l in f.readlines()]
print wordlist

for word in wordlist:
	md5 = hashlib.md5(word)
	print md5.hexdigest(), word
