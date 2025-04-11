
print(' Please seat, and respond this questions:\n')

Gryffindor = int(0)
Ravenclaw = int(0)
Hufflepuff = int(0)
Slytherin = int(0)

print(' Q1) Do you like Dawn or Dusk? \n\n 1) Dawn \n 2) Dusk \n')
answer = int(input('Choose your option: '))
if answer == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif answer == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print('Wrong input.')


print(" \nQ2) When I’m dead, I want people to remember me as: \n\n 1) The Good \n 2) The Great \n 3) The Wise\n 4) The Bold \n")
answer = int(input('Choose your option: '))
if answer == 1:
    Hufflepuff += 2
elif answer == 2:
    Slytherin += 2
elif answer == 3:
    Ravenclaw += 2
elif answer == 4:
    Gryffindor += 2
else:
    print('Wrong input.')

print(' \nQ3) Which kind of instrument most pleases your ear? \n\n 1) The violin \n 2) The trumpet \n 3) The piano\n 4) The drum \n')
answer = int(input('Choose your option: '))
if answer == 1:
    Slytherin += 4
elif answer == 2:
    Hufflepuff += 4
elif answer == 3:
    Ravenclaw += 4
elif answer == 4:
    Gryffindor += 4
else:
    print('Wrong input.')

if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
    print('\nYou are in Gryffindor!\n')
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
    print('\nYou are in Ravenclaw!\n')
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
    print('\nYou are in Hufflepuff!\n')
else:
    print('\nYou are in Slytherin!\n')
