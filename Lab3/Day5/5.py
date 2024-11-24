import os
import random
import string

# 原代码
os.makedirs('img',exist_ok=True)
s=set()
while len(s)<100:
	r=''.join(random.choices(string.ascii_uppercase + 
						string.digits, k=4))
	r+=".png"
	s.add(r)
for name in s:
	with open(os.path.join('img',name),'w') as file:
		pass

# 新代码
k=random.sample(sorted(s),50)
for name in k:
	newName = name.replace('.png','.jpg')
	os.rename(os.path.join('img',name),os.path.join('img',newName))
	