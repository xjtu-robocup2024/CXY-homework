def cacluate(*args):
	average = sum(args)/len(args)
	over = []
	for i in range(len(args)):
		if args[i] > average:
			over.append(i)
	return (average,over)

def main():
	pass

if __name__ == '__main__':
	main()