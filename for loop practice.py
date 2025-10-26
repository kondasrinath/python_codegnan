# sum of list using for loop

'''s = 0
lst = [1,2,3,6,79]
for i in lst:
    s = s+i
print(s)
'''

# product of list

''''s = 1
lst = [1,5,8,6,4]
for i in lst:
    s = s*i
print(s)
'''
# max val of lst

'''a = [2,5,8,9,234]
value = 0
for i in range(len(a) - 1):
    if a[i] > a[i+1]:
        value = a[i]
        print(value)
    else:
        print(value)
'''
    


# revese of num
'''n = 9876
s = str(n)
print(s[::-1])
'''

# if even square ,odd square root

'''a = [1,2,3,5,89]
res = []
for i in a:
    if i%2 == 0:
        res.append(round(i**0.5,3))
    else:
        res.append(i**2)
print(res)
'''

# continue
#break
#pass

'''n = int(input())
for i in range(1,11):
    if i == 8:
        break
    print(i*n)
'''

#the continue keyword skips following  the current execution and other iterations will done and execution we be held

#example:
'''for i in range(1,6):
    if i == 5:
       continue
print(i,end = " ")
'''


# the break statements terminates the loop when condition meets

for i in range(1,7):
   if i == 4:
       break 
   print(i)






































