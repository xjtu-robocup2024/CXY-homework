import os
import random

# 随机数文件的生成
with open('1.txt','w') as file:
	for i in range(10):
		t=[0]*3
		t = list(map(lambda x: random.random(),t))
		file.write(','.join(map(str,t))+'\n')

# 输出数据
t=[]
with open('1.txt','r') as file:
	for line in file:
		data = line.strip().split(',')
		t.append(float(data[1]))
average = sum(t)/len(t)
len = len(t)
median = 0
t.sort()
if len%2 == 0:
	median = (t[len//2]+t[len//2+1])/2
else:
	median = t[len//2+1]

print(f"Max:     {max(t)}")
print(f"Min:     {min(t)}")
print(f"Average: {average}")
print(f"Median:  {median}")