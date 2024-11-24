import random
with open('data.txt', 'w') as file:
	for i in range(100000):
		s = random.randint(1, 100)
		file.write(f"{s}\n")