#sets are unordered collections of unique objects
#sets are mutable and thus new elements can be added to them
basket={'apple','oranges','apple','pear','orange','banana'}
print(basket)
#operations of sets
#set does not allow duplicates
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a.intersection(b))
print(a.union(b))
print(a.difference(b)) #It returns the elements in a and not in b
print(b.difference(a))
#symmetric_difference returns all the difference elements in both sets
print(a.symmetric_difference(b))
#we can check if a number is in the set
print(1 in a)
print(len(a))
#adding values to a set
s1={
    1,2,3,4,5,6
}
print(s1)
s1.update([7,8,9,10])
print(s1)
s2={11,12,13,14,15}
s1.update(s2)
print(s1)
#removing values from a set
#we use remove or dicard
s1.remove(15)
print(s1)
s1.discard(14)
print(s1)

