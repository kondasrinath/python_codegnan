# def sum_of_numbers():
#     x = 20
#     y = 87
#     z = x+y
#     return z
# res = sum_of_numbers()
# print(res)


'''with parameters and without return'''
# def sum_of_numbers(num1,num2):
#     z = num1+num2
#     print(z)
#     return
# res = sum_of_numbers(10,20)
# print(res)

'''sum of numbers'''
# def sum_of_numbers():
#     a = 10
#     b = 20
#     c = a+b
#     print(c)
#     return
# tol = sum_of_numbers()
# print(tol)


'''with parameters and with return'''
# def numbers(num1,num2):
#     total = num1+num2
#     print("from function defination",total)
#     return total
# res = numbers(20,50)
# print("from function call",res)


'''to check even r odd'''
# def sum_of_even(num):
#     if num%2 == 0:
#         return True
#     else: return False
# a = 14
# n = sum_of_even(a)
# print(n)


'''odd numbers'''
# def sum_of_odd(num):
#     if num%2!= 0:
#         return True
#     else:
#         return False
# a = 13
# n = sum_of_odd(a)
# print(n)

'''even number'''
# def add():
#     for i in range(1,n):
#         if i%2 == 0:
#             print(i)
# n = int(input())
# add()

'''palindrome'''
# n = 121
# temp = str(n)

# if temp == temp[::-1]:
#     print("Palindrome")
# else:
#     print("not a palindrome")


''' variabl/arbitary length of positional arguments'''
#function defination

# def sum_of_nums(*args):
#     # print(type(args))
#     # print(args)
#     s = 0
#     for i in range(len(args)):
#         s += args[i]
#     return s
# #function call
# print(sum_of_nums())
# print(sum_of_nums(10))
# print(sum_of_nums(10,11,27))
# print(sum_of_nums(10,49,47,63,12,76))


'''positional argument with variable '''
#function defination 
# def sum_of_nums(a, *args):
#     # print(type(args))
#     # print(args)
#     s = 0
#     for i in range(len(args)):
#         s += args[i]
#     return s
# #function call
# #print(sum_of_nums())
# print(sum_of_nums(10))
# print(sum_of_nums(10,11,27))
# print(sum_of_nums(10,49,47,63,12,76))

'''variable length of keyword arguments'''
#function dedfination

# def fun(**kwargs):
#     total = 0
#     for item in kwargs.items():
#         print(f"{item[0]} : {item[1]}")
#         total += item[1]
#     return total     
# #function call
# print(fun(apple = 10, mango = 40, banana = 20)) 


'''positional arguments followed by keyword arguments'''

# def fun(a,*args,**kwargs):
#     print(a)
#     print(args)
#     print(kwargs)
# fun(10,20,30,40,n1=10,n2=30)

'''Tpes of variables'''
# 1.local
# 2.global
# 3.non local


'''define scope of variables'''
# x = 10        #global
# def outer():
#     y = 20              #local
#     print(y)
#     def inner():
#         z = 30                  #non local
#         print(z)
#     inner()
# outer()
# print()


'''using the global scope variable in local and global scope'''
# x = 10        #global
# def outer():
#     y = 20  local
#     a = y + x  local 
#     def inner(): 
#          z = 30    non local
#          b = x=y+z   non local
#          print("non local scope:",b)
#         inner()
#         print("local scope:",a)
# outer()
# print("blobal scope:",x)

'''the scope of variable in python defines the region of program where the variable is recognized and can be accessed'''
"""
1.global scope
2.local scope
3.non local scope
"""
# 1.global : the variables are defined outside the finction those variable calleds as global scope variables
# 2.local : the variables rae defined inside the function thoswe variables are called as local scope variables
# 3.non local : the variables rae defined inside the nested function(fun(fun )) those variables are called as nonlocal variables

# global variables can be access throughoutthe program but we cant update directly 
# by defining with one variable with global keyword we can update the global scope variable inside the local scope
# by defining the varible with non local keyword local variables we can update in non local scope 

'''update global in local with non local kw
updating local in non local with non local kw'''
# x = 10        #global
# def outer():
#     global x
#     x = x+1  #global scope variable update
#     y = 10    # local scope
#     def inner(): 
#          nonlocal y
#          y = y+2
#          print("non local scope:",y)
#         inner()
#         print("local scope:",y)
# outer()
# print("blobal scope:",x)