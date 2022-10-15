a=[]
n=int(input('enter the limites:'))
print ('enter the eliments:')
for i in range (0,n):
	k=int(input())
	a.append(k)
print('big number is:')
b=a[0]
for i in range (1,n):
	 if b<a[i]:
	      b=a[i]
print (b)
if b==a[0]:
	c=a[1]
else:
	c=a[0]
for i in range (1,n):
	if a[i]>c and b>a[i]:
	      c=a[i]
print(c)
















