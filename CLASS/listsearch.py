a=[]
n=int(input('enter the limites:'))
print ('enter the elements:')
for i in range (0,n):
	k=int(input())
	a.append(k)
#a.append(0) 
s=int(input('enter the limites:'))
#x=int(input('enter the index:'))
for i in range (0,n):
	if s==a[i]:
		print('the  element  is hear in the index', i )
		break
else:
	print('no')
#a[i]=a[i+1]
#print('the  element  is:')

#for i in range(0,n-1):
#	print(a[i])

















