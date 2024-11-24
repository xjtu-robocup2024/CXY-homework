X=[[12,7,3],
	 [4,5,6],
	 [7,8,9]]
Y=[[5,8,1],
	 [6,7,3],
	 [4,5,9]]
Z=X.copy()
for i in range(3):
	for j in range(3):
		Z[i][j]=X[i][j]+Y[i][j]
for i in range(3):
	print(Z[i])