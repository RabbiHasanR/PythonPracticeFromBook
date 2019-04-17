def is_prime2(n):
	if n==2:
		return True #2 is prime
	if n%2==0:
		print(n ,'is divided by 2')
		return False #all even numbers except 2 are not prime
	if n<2:
		return False #number less than 2 are not prime
	prime=True
	for x in range(3,n,2):
		if n%x==0:
			print(n, 'is divisible by ', x)
			prime=False
			return prime
	return prime
while True:
	number=input('Please enter a number (enter 0 to exit): ')
	number=int(number)
	if number==0:
		break
	prime=is_prime2(number)
	if prime is True:
		print(number,' is a prime number.')
	else:
		print(number,' is not a prime number.')
	