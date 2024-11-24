import os
for name in os.listdir('.'):
	filePath = os.path.join('.',name)
	if not os.path.isfile(filePath):
		continue
	with open(filePath, 'rb') as file:
		st = file.read()
	st = st.decode()
	st = st.replace('python','class')
	st = st.encode()
	with open(filePath, 'wb') as file:
		file.write(st)
	newName = name.replace('python','class')
	newPath = os.path.join('.',newName)
	os.rename(filePath,newPath)