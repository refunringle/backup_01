d=int(input('ENTER THE NUMBER:'))
b=0
i=0
while d>0:
	r=d%2
	b=b+(r*(10**i))
	i=i+1
	d=d//2
print('binery equalent is:',b)
