import turtle

def draw_square(side_length):
	turtle.color('red')
	turtle.speed(8)
	for i in range(4):
		turtle.forward(side_length)
		turtle.left(90)

counter=0
while counter<90:
	draw_square(100)
	turtle.right(4)
	print(counter)
	counter+=1

turtle.exitonclick()