import random

def guess_number():
    guess = int(input('Choose a number between 1 and 100: '))
    lifes = 9
    random_number = random.randint(1, 100)
    while (lifes > 0):
        print('You have ' + str(lifes) + ' lifes')
        if guess == random_number:
            print('Congratulations you win 🥳')
            break
        elif guess < random_number:
            lifes -= 1
            guess = int(input('Choose a higher number. Enter another number: '))
        elif guess > random_number:
            lifes -= 1
            guess = int(input('Choose a lower number. Enter another number: '))
    if lifes == 0:
        print('Oops you couldn´t make it😕  ¡Try again! ')
        

def run():
    print('Welcome! This game is four you to have some fun 😎 \n')
    print('How to play it: \n')
    print('The objective is that you guess a random number between 1 and 100. \nYou will have 10 lifes in order to guess the number, the system will give you some clues, so lets have some fun! 😋 \n \n')
    guess_number()  


if __name__ =='__main__':
    run()