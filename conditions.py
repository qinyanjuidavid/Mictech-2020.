people=20
cats=30
dogs=15
if people<cats:
    print('There are too many cats, This world is doomed')
if people>cats:
    print('There are few cats! This world is nice.')
#using else
'''
club=input('Enter the name of your club:')
if club.lower()=='mictech':
    print('Wow,Mictech is a nice club.')
else:
    print('Mhhh! sounds like a good club but i dont know it.')'''
#lets use elif statement now
num1=53
num2=33
num3=101
if num1>num2 and num1>num3:
    print(f'{num1} is the greatest number.')
    if num1>num2 and num2>num3:
        print(f'{num2} is the second greatest number.')
        if num1>num2 and num2>num3:
            print(f'{num3} is the smallest number.')
        else:
            print('This line is always printed.')
    elif num1>num3 and num3>num2:
        print(f'{num3} is the second greatest number.')
        if num1>num3 and num3>num2:
            print(f'{num3} is the smallest number.')
        else:
            print('This line is always printed')
    else:
        print('This line is always printed.')
elif num2>num1 and num2>num3:
    print(f'{num2} is the greatest number.')
    if num2>num1 and num1>num3:
        print(f'{num1} is the second largest number.')
        if num2>num1 and num1>num3:
            print(f'{num3} is the smallest number.')
        else:
            print('This line is always printed.')
    elif num2>num3 and num3>num1:
        print(f'{num3} is the second largest number.')
        if num2>num3 and num3 and num1:
            print(f'{num1} is the least number.')
        else:
            print('This line is always printed')
    else:
        print('This line is always printed.')
elif num3>num1 and num3>num2:
    print(f'{num3} is the greatest number.')
    if num3>num1 and num1>num2:
        print(f'{num1} is the second largest number.')
        if num3>num1 and num1>num2:
            print(f'{num2} is the least number.')
        else:
            print('This line is always printed.')
    elif num3>num2 and num2>num1:
        print(f'{num2} is the second largest number.')
        if num3>num2 and num2>num1:
            print(f'{num1} is the least number.')
        else:
            print('This line is always printed.')
    else:
        print('This line is always printed')
else:
    print('This line is always printed...')
#The above is a nested if statement however it does not include the ==
#you can try to check if the numbers are equal
#learn how to make decisions and dont just make scripts that make's decisions for themselves
#lets check if the years are leap or not
year=eval(input('Enter the year you want to check if it\'s leap year:'))
if year%4==0 and year%2==0:
    print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year.')
