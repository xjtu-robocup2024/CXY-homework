x=int(input())
y=int(input())
z=int(input())
if x>y:
	x,y=y,x
if y>z:
	y,z=z,y
if x>y:
	x,y=y,x
	
print("x = %d\ny = %d\nz = %d\n" % (x,y,z))