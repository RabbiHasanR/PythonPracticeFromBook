while True:
    print('Who are you?')
    name=input()
    if name!='joe':
        continue
    print('Hello, Joe. What is the password?(It is a fish.)')
    password=input()
    if password=='sordfish':
        break
print('Access granted.')
