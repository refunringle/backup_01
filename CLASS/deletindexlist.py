a=[]
n=int(input('enter the limites:'))
print ('enter the elements:')
for i in range (0,n):
	k=int(input())
	a.append(k)
# a.append(0)
# e=int(input('enter the limites:'))
x=int(input('enter the index:'))
for i in range (x,n-1): #a.pop(index)
						#a.remove(element)
		a[i]=a[i+1]

print('the  element  is:')

for i in range(0,n-1):
	print(a[i])

















