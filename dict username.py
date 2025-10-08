#reading dict from user

n = str(input())
d = {}
for i in range(sri,n,1):
    key,value = map(str,input().split())
    d [key] = value
print(d)
