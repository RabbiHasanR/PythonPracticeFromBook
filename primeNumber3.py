import math
import timeit #import for find how many time need to run program
def is_prime2(n=1013):
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

def is_prime3(n=1013):
	if n==2:
		return True #2 is prime
	if n%2==0:
		print(n ,'is divided by 2')
		return False #all even numbers except 2 are not prime
	if n<2:
		return False #number less than 2 are not prime
	m=math.sqrt(n)
	m=int(m)+1
	for x in range(3,m,2):
		if m%x==0:
			print(n, 'is divisible by ', x)
			return False
	return True
	

t1=timeit.timeit(is_prime2)
t2=timeit.timeit(is_prime3)
print(t1,t2,t1/t2) #find  runtime difference between is_prime2 and is_prime3