a=[]
n=int(input('enter the limites:'))
print ('enter the elements:')
for i in range (0,n):
	k=int(input())
	a.append(k)
#a.append(0) 
#s=int(input('enter the limites:'))
#x=int(input('enter the index:'))
for i in range (0,n):
	for j in range (0,n-i-1):
		if  a[j]>a[j+1]:
			t=a[j]
			a[j]=a[j+1]
			a[j+1]=t
print('the  sort element  is:')
for i in range(0,n):
	print(a[i])

















