a=[]
n=int(input('enter the limites:'))
print ('enter the eliments:')
for i in range (0,n):
	k=int(input())
	a.append(k)
a.append(0)
e=int(input('enter the limites:'))
x=int(input('enter the index:'))
for i in range (n,x,-1):
	a[i]=a[i-1]
a[x]=e
print('the  eliment  is:')

for i in range(0,n+1):
	print(a[i])

















