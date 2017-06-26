a=[2,34,45,43,56,65,55,87,99]
b=len(a)
c=[0]

for i in range(b):
	d=min(a)
	a.remove(d)
	c.append(d)
	
print c
