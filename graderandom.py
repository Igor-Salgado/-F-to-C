import random

grade = random.randint(0, 100)

if grade > 55:
    print(f"Your grade is: {grade}. You passed!")
else:
    print(f"Your grade is: {grade}. You failed.")
