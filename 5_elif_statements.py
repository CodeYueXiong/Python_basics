my_num = 5.0
if my_num % 2 == 0:
    print("Your number is even")
elif my_num % 2 != 0:
    print("Your number is odd")
else:
    print('Are you sure your number is an integer')

dice_value = 32
if dice_value == 1:
    print('You rolled a {}. Great job!'.format(dice_value))
elif dice_value == 2:
    print('You rolled a {}. Great job!'.format(dice_value))
elif dice_value == 3:
    print('You rolled a {}. Great job!'.format(dice_value))
elif dice_value == 4:
    print('You rolled a {}. Great job!'.format(dice_value))
elif dice_value == 5:
    print('You rolled a {}. Great job!'.format(dice_value))
elif dice_value == 6:
    print('You rolled a {}. Great job!'.format(dice_value))
else:
    print("None of the conditions above (if elif) were valid inputs in a dice!")

## assigned tasks
num = 10
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print('Fizz')
elif num % 5 == 0:
    print('Buzz')
else:
    print(str(num))