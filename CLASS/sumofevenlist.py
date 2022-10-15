a=[]
n=int(input('ENTER THE NUMBER:'))
print('enter the elements:')
for i in range(0,n):
	k=int(input())
	a.append(k)

print(' list elements are :')
s=0
for i in range(0,n):
	if a[i]%2==0:
		s=s+a[i]
print('sum is:',s)	

#print(' list elements are :')
#for i in range(0,n):
#	print(a[i])