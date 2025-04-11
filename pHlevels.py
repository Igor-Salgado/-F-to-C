import random

ph = random.randint(0, 14)

if ph > 7:
    print(f'Your pH is: {ph}. Basic.')
elif ph < 7:
    print(f'Your pH is: {ph}. Acid.')
else:
    print(f'Your pH is: {ph}. Neutral.')
