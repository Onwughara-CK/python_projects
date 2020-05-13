from random import randint
player = input('What is your name:')
secretNum = randint(1, 20)
print(secretNum)

for guessNum in range(1, 7):
    guess = int(input(f'{player}, guess a number between 1 and 20:'))

    if guess > secretNum:
        print(f'{guess} is larger than the secret number')
    elif guess < secretNum:
        print(f'{guess} is smaller than the secret number')
    else:
        break
if guess == secretNum:
    print(
        f'congratulations {player}, your guess is as good as mine. and you got it after {guessNum} guesses')
else:
    print(f'{player}, you have run out of your guess limit')
