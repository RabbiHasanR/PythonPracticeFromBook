import turtle
turtle.color('blue')
turtle.speed(5)

counter=0
while counter<36:
	for i in range(4):
		turtle.forward(100)
		turtle.right(90)
	turtle.right(10)
	print(counter)
	counter+=1
turtle.exitonclick()
