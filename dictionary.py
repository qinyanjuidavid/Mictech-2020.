#A dictionary is simply a collection data type that stores a key and a value
sample={
    'key':'value',
}
East_africa={
    'Kenya':'Nairobi',
    'Uganda':'Kampala',
    'Tanzania':'Dodoma'
}
print(East_africa)
print(East_africa['Kenya'])
East_africa["Burindi"]='Kigali'
print(East_africa)
print(East_africa.get('Ethiopia','Seems This country is not in the East Africa community'))
#Iterating the dictionary
#Iteration is the ability to execute a certain code repeatedly
for key,value in East_africa.items():
    print(f"{key} - {value}")
#Let's relate to The real world
phone={
    'John':['07569595','johndoe@gmail.com'],
    'Maggy':'188928989',
    'Ken':'6497995454',
    'lucy':'99765655',
    'Jane':'2549555554'
}
print(phone['John'][1])
while True:
    name=input('-:')
    print(phone.get(name,'No such results'))

