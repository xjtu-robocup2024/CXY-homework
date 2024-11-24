import os
import random
import string

# 创建随机文件
i = int(input('随机文件个数：'))
j = int(input('文件行数：'))
files = set()
while len(files) < i:
	st = ''.join(random.choices(string.ascii_uppercase+string.digits,k=5))
	files.add(st)
os.makedirs('test',exist_ok=True)
for f in files:
	with open(os.path.join('test',f+'.txt'), 'w') as file:
		for _ in range(j):
			file.write(random.choice(string.printable)+'\n')

# 每⼀个⽂件的所有⾏后⾯增加-python
for file in os.listdir('test'):
	filePath = os.path.join('test',file)
	if not os.path.isfile(filePath):
		continue
	with open(filePath, 'r') as f:
		fileContent = f.readlines()
	fileContent = [_.replace('\n',' -python\n') for _ in fileContent]
	with open(filePath, 'w') as f:
		f.writelines(fileContent)
	newName = file.replace('.',' -python.')
	os.rename(filePath,os.path.join('test',newName))