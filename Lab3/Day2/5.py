a=[] # 质数表
for i in range(2,201):
	flag = True
	for j in range(2,len(a)):
		if i%j==0:
			flag=False
			break
	if flag:
		a.append(i)
		if i>100:
			print(i,end=" ")