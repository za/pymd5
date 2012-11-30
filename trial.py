import hashlib

wordlist = ['admin','password']

for word in wordlist:
	md5 = hashlib.md5(word)
	print md5.hexdigest()
