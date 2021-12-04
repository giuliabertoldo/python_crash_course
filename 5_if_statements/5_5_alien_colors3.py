# 5.2 IF STATEMENTS
## EXERCISE 5-4
alien_color = 'green'

if alien_color == 'green':
    print("5 points earned")
elif alien_color == 'yellow':
    print('10 points earned')
elif alien_color == 'red':
    print('15 points earned')

print('\n')
alien_colors = ['green', 'yellow', 'red']

for color in alien_colors:
    if color == 'green':
        print("5 points earned")
    elif color == 'yellow':
        print('10 points earned')
    elif color == 'red':
        print('15 points earned')
