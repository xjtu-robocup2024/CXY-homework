a=int(input())
st=str(a)
print("位数：%d"%len(st))
print("逆序打印：",end="")
for i in range(len(st)-1,-1,-1):
	print(st[i],end="")
