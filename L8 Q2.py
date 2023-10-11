n=int(input("enter the no of elements:"))
l=list()
for i in range(n):
    l.append(int(input("enter a number:")))
m=[]
for j in range(n):
    s=min(l)
    m.append(s)
    l.remove(s)
print("the sorted list is:",m)