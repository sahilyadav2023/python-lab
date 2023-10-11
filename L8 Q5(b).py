n=int(input("enter no of elements:"))
l=[]
s=0
for i in range(n):
    a= int(input("enter a string:"))
    l.append(a)
print("the list is ",l)
newl=[]
for i in l:
    if i>0:
        newl.append(i**2)
    else:
        newl.append(0)
print("the new list is",newl)