a=[0,1]
for i in range(2,20):
	a.append(a[-1]+a[-2])
print(a)