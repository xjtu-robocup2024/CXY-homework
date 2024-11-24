h=100
s=-h
for i in range(10):
	s+=h*2
	h/=2
print("第10次落地时，共经过 %f ⽶" % s)
print("第10次反弹高度为 %f 米" % h)