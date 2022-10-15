a=[]
n=int(input('ENTER THE NUMBER:'))
print('enter the elements:')
for i in range(0,n):
	k=int(input())
	a.append(k)

print(' list elements are :')
c=a[0]
for i in range(1,n):
	if a[i]>c:
		c=a[i]
print(c)	

#print(' list elements are :')
#for i in range(0,n):
#	print(a[i])