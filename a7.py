a="restart"
b=list(a)
c=len(b)
i=0
while (i<c-1):
	j=i+1
	while (j<c-1):
		if b[i]==b[j]:
			b.remove(a[j])
			b.insert(j,"$")
		j=j+1
"".joina()
print a
