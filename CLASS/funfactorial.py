def factorial (n):
	fact=1
	for  i in range(2,n+1):
		fact=i*fact
	return fact
n=int(input("enter the value:"))

fact=factorial(n)
print(fact)

