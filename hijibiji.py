import turtle
import random
#list of colors
colors=['red','green','blue','yellow','orange','black','purple']
turtle.penup()
for i in range(20):
	x=random.randint(-200,200)
	y=random.randint(-200,200)
	#set a random position
	turtle.setposition(x,y)
	#set a random color
	i=random.randint(0,len(colors)-1)
	turtle.dot(colors[i])

turtle.exitonclick()