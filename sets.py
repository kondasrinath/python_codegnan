# characteristics  of sets
'''not allow duplicates
unordered collection
{}
mutable
sets are not index based
set allow only hashable datatype
all set elements we can use as dictionar keys '''




# set {} is a unordered collection differeent datatype with unique elements and it is denotes with {}


#operations
'''
union
intersection
difference
symmetric difference
issubset
issuperset
isdisjointset
'''

#examples on sets

'''s1 = {1,2,3,4,5}
s2 = {1,2,0,8,7}
print(s1.union(s2))''' # logic of operations

'''s = {1,2,3,4,5,98.87,"Srinath",(9876),2,1}
print(s)'''

'''s = set(map(int,input().split()))   # set user input
print(s)'''


#set operations
s1 = {1,2, "Hi","SRINATH"}
s2 = {"PYTHON","DEVELOPER"}
print("Union:",s1.union(s2))
print("Intersection:",s1.intersection(s2))
print("Difference:",s1.difference(s2))
print("Symmentric Difference:",s1.symmetric_difference(s2))
print("Sub Set:",s1.issubset(s2))
print("Super Set:",s1.issuperset(s2))
print("Dis joint set:",s1.isdisjoint(s2))




