st=input()
letter,space,number,other=0,0,0,0
for i in range(len(st)):
	if st[i]>='a' and st[i]<='z' or st[i]>='A' and st[i]<='Z':
		letter+=1
	elif st[i]==' ':
		space+=1
	elif st[i]>='0' and st[i]<='9':
		number+=1
	else:
		other=1
print("letter\t=%d\nspace\t=%d\nnumber\t=%d\nother\t=%d\n"%(letter,space,number,other))