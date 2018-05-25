import random

print('---------------------------')
print('     GUESS THE NUMBER')
print('---------------------------')
print()

success = False
answer = random.randint(0, 100)

guess_str = input('Guess a number between 0 and 100: ')
guess = int(guess_str)


while not success:
    if guess == answer:
        success = True
        print( 'YES! You\' got it. the number was ', answer )
        continue
    elif guess < answer:
        print('Sorry but ', guess, 'is LOWER than the number')
    elif guess > answer:
        print('Sorry but ', guess, 'is HIGHER than the number')

    guess_str = input('Guess a number between 0 and 100: ')
    guess = int(guess_str)


