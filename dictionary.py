

# Dictionary:
#dictionary is a ordered collection of key value pairs and it is denotes with {}.
#dict representiation    {key:value}


#characteristics
'''
it is mutable
unique key values
values allows duplicates
only hashable datatypes acts as keys
values access by passing keys
it is not index based'''

# Empty dictionary representiation


#example
'''d = {1:"s","s":1,"hi":"hello",(10.234):(20.23)}
print(d)'''

#list cant be used here

# values access by passing keys
'''d = {1:"s","s":2,(1232):(123),(123.23):(678.0987)}
print(d)
print(d[1]) # in {key or value we have to call index if the value is present}
print(d["s"]) #suppose we are calling with "s" the op will be 2
print(d[2])'''

# empty dictionary representiation
'''d1 = {}
d2 = dict()
print(type(d1))
print(type(d2))'''

# methods
'''get(key,default) - it returns the value if key is present in dictionary,otherwise default value
upaste(new_dict) - it updates the dictionary with new-dict items
popitem(key) - it return and removes the item if key is present in dict.otherwise last "key Error"
popitem()- it returns and removes last itenm
keys()- returns list of keys
values()-returns list values
items()-returns the list of tuole of key value pairs
clear() - removesc all  items from dict'''

d = {1:"srinath",2:"konda",(123):(198),(234):(254),(123.45):(987)}
print(d.get(1))
print(d.keys())
print(d.popitem())
print(d.values())
print(d.items())





