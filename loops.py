#For loop
#loops are essential for doing a repetetive task in a script
fruits=['Bananas','Oranges','Mangoes','watermelons']
for fruit in fruits:
    print(f'I love {fruit}.')
#range(start, stop, increament)
print(list(range(5)))
for i in range(5):
    print('Hello Mictech.')

for number in range(20,41):
    print(number)
for n in range(0,100,2):
    print(n)


#summing up numbers in a range
count=0
for number in range(1,4):
    count+=number
print(f'sum= {count}')
#While loop
x=0
while x<=20:
    print(x)
    x+=1
#even and odd numbers
for z in range(0,100):
    if z%2==0:
        print(f'Even- {z}')
    else:
        print(f'Odd- {z}')
#multiplication table
for num in range(1,11):
    for num1 in range(1,11):
        print(f'{num} * {num1}={num*num1}')
    print("\n")
#pattern
for i in range(0,11):
    for x in range(0,i):
        print("*",end=" ")
    print("\n")
