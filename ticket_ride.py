
print(' How tall are you and how many coins do you have? ')

try:

    height = int(input('Height: '))
    credits = int(input('Credits: '))

    if height >= 137 and credits >= 10:
        print('Enjoy the ride!')
    elif height >= 137 and credits < 10:
        print("You don't have enough credits.")
    elif height < 137 and credits >= 10:
        print('You are not tall enough to ride.')
    else:
        print("You don't meet either requirements.")

except ValueError:
    print("Please enter valid numbers!")
