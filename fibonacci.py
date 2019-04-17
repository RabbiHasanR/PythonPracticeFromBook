#import turtle
fib_x=1
fib_next=1
n=input()
n=int(n)
if n<=2:
	fib_n=1
else:
	print(fib_x)
	print(fib_next)
	#turtle.circle(fib_x,180)
	#turtle.circle(fib_x,180)
	i=3
	count=0
	while i<=n:
		i+=1
		count+=1
		fib_temp=fib_x+fib_next
		fib_x=fib_next
		fib_next=fib_temp
		#turtle.circle(fib_next,180)
		print(fib_next)
	fib_n=fib_next
	print('Total count:', count)
#print(fib_n)