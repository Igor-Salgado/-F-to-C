
import random

question = input('Question: ')

magic8 = random.randint(1, 9)

if magic8 == 1:
    print('Yes - definitely.')
elif magic8 == 2:
    print('It is decidedly so.')
elif magic8 == 3:
    print('Without a doubt.')
elif magic8 == 4:
    print('Reply hazy, try again.')
elif magic8 == 5:
    print('Ask again later.')
elif magic8 == 6:
    print('My sources say no.')
elif magic8 == 7:
    print('Outlook not so good.')
else:
    print('Very doubtful.')
