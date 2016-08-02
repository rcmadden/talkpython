import random

print('------------------------------------')
print('          GUESS THE NUMBER')
print('------------------------------------')

the_number = random.randint(0, 100)
guess = -1

while guess != the_number:
    guess = input("Guess a number between 1-100: ")
    guess = int(guess)
    if guess == the_number:
        print('Great guess, you won, my number was {}'.format(the_number))

    elif guess > the_number:
        print('Your guess of {} to high'.format(guess))

    elif guess < the_number:
        print('Your guess is to low')
print("Done.")

