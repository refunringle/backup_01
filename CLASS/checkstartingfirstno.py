n=int(input('enter the number:'))
y=int(input('enter the digit:'))

i=0
while n>i:
	d=n%10
	a=d
	n=n//10
if a==y:
 	print('done')
else:
	print('no')