a=1,2,3,4,5
b=1,2
print(f"type(a)={type(a)}, type(b)={type(b)}")
print(a)
print(b==(1,2))
# Python 将用逗号分隔的变量看成元组并赋值给a,b

a={}
a[1]=2
a[1,2]=1
print(a)
print(a[1,2])
# a是字典性变量，其索引可以为整数或元组

a=[[1,2,3],[1,2,3]]
print(a[1][2])
print(a[1,2])
# 不能把元组作为二维数组的索引