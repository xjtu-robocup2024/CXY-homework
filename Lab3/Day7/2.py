import random
import string
import os
i = int(input("行数："))
with open('test.txt','w') as file:
	for j in range(i):
		line = ''.join(random.choice(string.printable) for _ in range(8))
		file.write(line+'\n')
dstFile = ''
with open('test.txt','rb') as src, open('copy_test.txt','wb') as dst:
	dst.write(src.read())