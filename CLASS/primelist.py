a=[]
n=int(input('ENTER THE NUMBER:'))
print('enter the elements:')
for i in range(0,n):
	k=int(input())
	a.append(k)

print(' prime  element is :')
for i in range(0,n):
	for j in range (2,a[i]):
		if a[i]%j==0:
			break
		if a[i]==j+1:
		
			print(a[i])	


