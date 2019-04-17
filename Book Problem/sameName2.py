def spam():
    global eggs #this is the global
    eggs='spam'
    print(vacon)

def bacon():
    eggs='bacon' #this is the local

def ham():
    print(vacon) #this is the global

vacon='global' #this is the global
eggs='eggs' #this is the global
spam()
print(eggs)
