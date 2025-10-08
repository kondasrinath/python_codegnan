'''Tuples- tuple is a ordered collection of different datatype element and it is immutable
it is defines with ()
#characteristics of tuple
immutable
it is hetero geneous
index based and slicable
ordered collection'''


'''t1 = tuple(map(int,input().split())) # to find integers
t2 = tuple(map(str,input().split()))# to find strings
print(type(t1))
print(type(t2))'''

#t = tuple(map(int,input().split()))
#print(t)

# index based and slicable
'''t = (1,2,3,[10,20,20],"srinath")
#print(t[0])
#print(t[-1])
#print(t[-4])
#print(t[-1:2:-1])
#print(t[3:4:-1])'''


# single element representation in tuple
'''t = (29)
t1 = [20]
t2 = (2,)
print(type(t)) #class int
print(type(t1)) # class list
print(type(t2)) # class tuple '''


# tuple operations
# concatination
'''t1 = (1,2,3)
t2 = ("a" ,"b")
print(t1+t2)'''

# repetation
'''t1 = (1,2,3)
print(t1 * 3)'''


# tuple methods

'''t1= (1,2,3,4)
ind = t1.index(3)
cnt = t1.count(3)
print(ind,cnt)'''

# built in functions

'''t = (1,2,3,5,7,9)
print(min(t),max(t),len(t),sum(t))'''

# string to tuple
s = "srinath"
print(list(s))
print(tuple(s))
# tuple to list coversion

t = (1,2,3,4,5,9)
print(list(t))
