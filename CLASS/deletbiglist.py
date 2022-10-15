a=[]
n=int(input("enter the element:"))
print('enter the element:')
for i in range(0,n):
	k=int(input())
	a.append(k)
b=int(input('enter the element:'))
for i in range(0,n):
	if a[i]>b:
		print (a[i])
