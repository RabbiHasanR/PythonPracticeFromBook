import random
def getAnswer(answerNumber):
    if answerNumber==1:
        return 'It is certain'
    if answerNumber==2:
        return 'It is decidedly so'
    if answerNumber==3:
        return 'yes'
    if answerNumber==4:
        return 'Reply hazy try again'
    if answerNumber==5:
        return 'Ask again later'
    if answerNumber==6:
        return 'Concentrate and ask again'
    if answerNumber==7:
        return 'My reply is no'
    if answerNumber==8:
        return 'Outlook not so good'
    if answerNumber==9:
        return 'Very doubtful'


number=random.randint(1,9)
fortune=getAnswer(number)
print(fortune)
None==fortune
