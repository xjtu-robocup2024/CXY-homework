with open('test.txt','rb') as file:
	content = file.read()
with open('test.txt','wb') as file:
	file.write(b'python\n')
	file.write(content)
	file.write(b'python\n')