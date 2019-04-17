def collatz(number):
    if number%2==0:
        return number//2
    else:
        return 3*number+1

print('Enter Number:')
try:
    number=int(input())
    result=collatz(number)
    while True:
        print(result)
        if result==1:
            break
        result=collatz(result)
except ValueError:
    print('Error: must enter integer')
    

