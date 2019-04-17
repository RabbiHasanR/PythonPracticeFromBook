def spam():
    eggs='spam local'
    print(eggs)

def vacon():
    eggs='vacon local'
    print(eggs)
    spam()
    print(eggs)

eggs='global'
vacon()
print(eggs)
