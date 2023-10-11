n=int(input("enter no of elements:"))
l=[]
s=0
for i in range(n):
    a= str(input("enter a string:"))
    l.append(a)
print("the list is ",l)
b=str(input("enter a string to search:"))
for j in l:
    if b==j:
        s=s+1
print(f'the string {b} is repeated {s} times ')