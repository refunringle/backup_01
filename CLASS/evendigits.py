n=int(input('ENTER THE NUMBER:'))
s=0
while n!=0 :
  d=n%10
  d=d*d
  s=s+d
  n=n//10
print('sum of digits is:',s)