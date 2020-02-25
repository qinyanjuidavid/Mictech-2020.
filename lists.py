#A list a collection data type that is similar to an array in other languages
fruits=['Apple','Banana','Mango','Pineapple','Orange']
print(type(fruits))
#accessing the elements in the fruits
print(fruits[0])
print(fruits[1:3])
print(fruits[-1])
print(fruits[-4])
#lists are mutable meaning that they can be changed
fruits[2]='Watermelon'
print(fruits)
#we can also add elements in our list
fruits.append('passion fruit')
print(fruits)
#We can add an element to a particular index
fruits.insert(1,'Avocado')
print(fruits)
#joining two lists together
vegetables=['sukuma wiki','tomatoes','onion','cabbages','spinach']
fruits.extend(vegetables)
print(fruits)
#We can remove an element from our list
fruits.remove('passion fruit')
print(fruits)
fruits.pop(1)
print(fruits)
print(len(fruits))
print(fruits.index('onion'))
fruits.append("Orange")
print(fruits)
print(fruits.count('Orange'))
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
#iterating through our list
for element in fruits:
    print(f"I love {element}")

even=[0,2,4,6,8,10,12,14,16,18,20]
for num in even:
    print(num)
#iterating a list
myHobby=["football",'swimming','reading','cycling','eating']
for element in range(len(myHobby)):
    #The second f statement requires indexing
    print(f'{element} I love {myHobby[element]}.')
