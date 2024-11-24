st=str(int(input()))
flag = True
for i in range(len(st)):
	if st[i] != st[-i-1]:
		flag = False
		break
print(flag)