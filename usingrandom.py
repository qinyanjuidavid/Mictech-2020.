import random
print(random.randint(0,100))
print(random.randrange(0,100,5))
#random with sequences(string,list,
my_list=[1,3,5,7,9]
print(random.choice(my_list))

#Dice game
'''
while True:
    choices=range(1,6)
    attempt=eval(input('Enter your choice:'))
    computer_choice=random.choice(choices)
    if attempt==computer_choice:
        print("Congraturations!!! You got it right.")
    else:
        print(f'Failed!!! The computers guese is {computer_choice}')
'''
#playing with numbers
'''
while True:
    choices=range(1,100)
    my_input=eval(input('Enter your guese:'))
    computers_choice=random.choice(choices)
    if my_input==computers_choice:
        print(f'Congratulations!!! you got it right. The answer is {computers_choice}')
    elif my_input!=computers_choice:
        if my_input>=1 and my_input<=100:
            if computers_choice>=51:
                print('The computer\'s choice is greater than 50.')
            elif computers_choice<=50:
                print('The computer\'s choice is less than 50.')
            else:
                print('This line is always printed.')
        else:
            print('Invalid Entry!!! Please enter a number that is between 1 and 100.')
    else:
        print('This line is always printed.')
'''
print('DO YOU WANNA PLAY THE ROCK, PAPER, SCISSORS.')
print('=' * 10)
while True:
    choices=['rock','paper','scissors']
    myChoice=input('Enter your choice-:').lower()
    computers_choice=random.choice(choices)
    if myChoice=='rock' or myChoice=='paper' or myChoice=='scissors':
        if myChoice=='rock':
            if computers_choice=='rock':
                print(f'It\'s a tie. The computer also choose {computers_choice}')
            elif computers_choice=='paper':
                print(f'You lose!!! The computer choose {computers_choice}')
            elif computers_choice=='scissors':
                print(f'Congrats!!! You won.')
            else:
                print('This line is always printed ')
        if myChoice=='scissors':
            if computers_choice=='scissors':
                print(f'It\'s a tie. The computer choose {computers_choice}.')
            elif computers_choice=='rock':
                print(f'You lose. The computer choose {computers_choice}')
            elif computers_choice=='paper':
                print('Congrats!!! You won.')
            else:
                print('This line is always printed.')
        if myChoice=='paper':
            if computers_choice=='paper':
                print(f'It\'s a tie. The computer also choose {computers_choice}.')
            elif computers_choice=='rock':
                print(f'Congrats!!! You won.')
            elif computers_choice=='scissors':
                print(f'You lose. The computer choose {computers_choice}.')
    else:
        print(f'Invalid input. please enter a choice from the list.{choices}')

