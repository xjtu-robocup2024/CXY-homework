import math

class Point:
	def __init__(self,x,y,z=0):
		self.x=x
		self.y=y
		self.z=z
		print("创建了"+str(self))
	def __del__(self):
		print("销毁了"+str(self))
	def __str__(self):
		return f"Point({self.x}, {self.y}, {self.z})"
	def __add__(self, other):
		if isinstance(other, Vector):
			return Point(self.x+other.x,self.y+other.y,self.z+other.z)
		if isinstance(other, Point):
			raise TypeError("Point + Point 不合法")
		raise TypeError()
	def __sub__(self, other):
		if isinstance(other, Vector):
			return Point(self.x-other.x,self.y-other.y,self.z-other.z)
		if isinstance(other, Point):
			return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
		raise TypeError()
	def __eq__(self, other):
		if not isinstance(other, Point):
			return False
		return self.x==other.x and self.y==other.y and self.z==other.z
	def __lt__(self, other):
		if not isinstance(other, Point):
			return False
		return self.x**2+self.y**2+self.z**2 < other.x**2+other.y**2+other.z**2
class Vector:
	def __init__(self,x,y,z=0):
		self.x=x
		self.y=y
		self.z=z
		print("创建了"+str(self))
	def __del__(self):
		print("销毁了"+str(self))
	def __str__(self):
		return f"Vector({self.x}, {self.y}, {self.z})"
	def __add__(self, other) -> 'Vector':
		if isinstance(other, Vector):
			return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
		raise TypeError()
	def __sub__(self, other) -> 'Vector':
		if isinstance(other, Vector):
			return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
		raise TypeError()
	def __eq__(self, other):
		if not isinstance(other, Vector):
			return False
		return self.x==other.x and self.y==other.y and self.z==other.z
	def __lt__(self, other):
		if not isinstance(other, Vector):
			return False
		return self.x**2+self.y**2+self.z**2 < other.x**2+other.y**2+other.z**2
	
	# 这里并没有给出旋转轴，这里认为向量绕z轴旋转。
	def __mul__(self, x):
		if isinstance(x, (int,float)):
			x = x * math.pi / 180
			return Vector(self.x*math.cos(x)-self.y*math.sin(x),
								 self.x*math.sin(x)+self.y*math.cos(x),
								 self.z)
		raise TypeError()
	def __truediv__(self, x):
		return self*(-x)
	