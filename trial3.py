#!/usr/bin/python

import hashlib

with open('sample_01.wl','r') as f: 
	wordlist = [l.strip() for l in f.readlines()]

print wordlist
