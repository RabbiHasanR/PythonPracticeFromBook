import turtle
turtle.shape('turtle')

for side_length in range(50,100,10):
	for i in range(4):
		turtle.forward(side_length)
		turtle.left(90)
	print(side_length)
turtle.exitonclick()