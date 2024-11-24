class Person:
	def __init__(self):
		self.name    = ""
		self.age     = 0
		self.gender  = ""
	def personInfo(self):
		print(f"Name:    {self.name}")
		print(f"Age:     {self.age}")
		print(f"Gender:  {self.gender}")
	def __str__(self) -> str:
		return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
class Student(Person):
	def __init__(self):
		super().__init__()
		self.college = ""
		self.Class   = ""
	def personInfo(self):
		super().personInfo()
		print(f"College: {self.college}")
		print(f"Class:   {self.Class}")
	def __str__(self) -> str:
		return f"Name: {self.name}, Age: {self.age}, \
Gender: {self.gender}, College: {self.college}, Class: {self.Class}"
