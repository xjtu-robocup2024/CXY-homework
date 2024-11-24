n=0
for i in range(1,5):
	for j in range(1,5):
		if i == j:
			continue
		for k in range(1,5):
			if i == k or j == k:
				continue
			s=i*100+j*10+k
			print(s)
			n=n+1
print("总数为：%d" % n)
