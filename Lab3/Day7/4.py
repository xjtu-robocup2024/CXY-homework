with open('test.txt','r') as file1, open('copy_test.txt','r') as file2:
	f1 = file1.readlines()
	f2 = file2.readlines()
len1 = len(f1)
len2 = len(f2)
for i in range(max(len1,len2)):
	flag = False
	if i>=len1 or i>=len2:
		flag = False
	elif f1[i] == f2[i]:
		flag = True
	if(not flag):
		print(i)
