import turtle

def draw_triangel(side_length):
	for i in range(3):
		turtle.forward(100)
		turtle.left(120)
		
draw_triangel(100)
turtle.exitonclick()
	