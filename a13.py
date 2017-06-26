n=input("enter the number:")
a=[]
for i in range(n):
	b=input()
	a.append(b)
	if (a[i]%2==0):
		i=i+1
		print 'even'
	else:
		print'odd'
		
