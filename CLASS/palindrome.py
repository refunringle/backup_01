n=int(input('ENTER THE NUMBER:'))
r=0
t=n

while n>0:
	d=n%10
	r=(r*10)+d
	n=n//10
if r==t:
   print('given number is palindrone')
else:
   print('given number is not palindrone')
# python rought.py
