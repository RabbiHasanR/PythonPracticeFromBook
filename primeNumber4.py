import math
def is_prime(n):
	if n<2:
		return False
	if n==2:
		return True
	if n%2==0:
		return False
	m=math.sqrt(n)
	m=int(m)+1
	for y in range(3,n,2):
		if n%y==0:
			return False
	return True

number1=input('Plese enter first number: ')
number2=input('Plese enter second number: ')
number1=int(number1)
number2=int(number2)
if number1>number2:
	temp=number1
	number1=number2
	number2=temp
	count=0
for x in range(number1,number2):
	if is_prime(x) is True:
		print(x)
		count+=1
print("Total prime number: ",count)		
			