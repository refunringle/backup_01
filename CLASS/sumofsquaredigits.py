n=int(input('ENTER THE NUMBER:'))
r=0
while n!=0 :
  d=n%10
  r=(r*10)+d
  n=n//10
print('reverse is:',r)