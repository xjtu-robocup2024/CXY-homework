def Insert(a:list, k):
	loc = len(a)
	for i in range(len(a)):
		if k < a[i]:
			loc = i
			break
	a.insert(loc, k)
	
def main():
	pass

if __name__ == '__main__':
	main()