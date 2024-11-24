a=input("指定的数字：")
n=int(input("指定的项数："))
st=""
s=0
for i in range(n):
	st=st+a
	s+=int(st)
print(s)