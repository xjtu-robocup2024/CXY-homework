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
