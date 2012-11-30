#!/usr/bin/python

import hashlib

f = open('/home/za/dev/github/id-wordlist/00-indonesian-wordlist.lst','rU')

wordlist = [l.strip() for l in f.readlines()]
print wordlist

for word in wordlist:
	md5 = hashlib.md5(word)
	print md5.hexdigest()+':'+word
