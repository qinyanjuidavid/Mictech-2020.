#function is basically a block of codes doing a particular task
#when writing functions we normally use def which means define
#All the lines inside the function are indented
def naming(first_name,last_name):
    print(f'My name first name is {first_name} and my last name is {last_name}.')

naming('David','Kinyanjui')
naming('John','Doe')
naming('Jane','Doe')
#We can establish The arguments,
#'*' This sign is called the asterisk
def country(*args):
    arg1,arg2,arg3=args
    print(f'I have travellered to the following places:\n{arg1}\n{arg2}\n{arg3}')
country('Nairobi','Mombasa','Nakuru')
#functions can return something
def simple(*args):
    num1,num2,num3=args
    sum=num1+num2+num3
    print(sum)
simple(5,5,6)
def simple1():
    print('My first function')
simple1()
def plus_ten(a):
    return a+10
print(plus_ten(2))
print(plus_ten(5))
print(plus_ten(6))
#Below is a function inside a function
def wage(w_hours):
    return w_hours*25
def with_bonus(w_hours):
    return wage(w_hours)+50
print(wage(8),with_bonus(8))
print("=="*100)
#Another function  inside a function
def salary(basic_salary,bonus):
    return f"Total salary: {basic_salary+bonus}"
def after_tax(tax_rate,basic_salary,bonus):
    total_salary=(basic_salary+bonus)
    total_tax=total_salary*tax_rate
    taxable_income=total_salary-total_tax
    return f'''The total tax is: {total_tax}.
The taxable income is: {taxable_income}'''
print(salary(40000,5000))
print(after_tax(0.12,40000,5000))
#This is another method of writing a function
def myNumbers(a=5,b=6,c=4):
    sum=a+b+c
    return sum
print(myNumbers())
