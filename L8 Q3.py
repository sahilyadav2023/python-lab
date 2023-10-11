n=int(input("enter the no of elements:"))
l=[]
for i in range(n):
    l.append(int(input("enter the elements here")))
for j in range(0,n):
    for k in range(j+1,n):
        if l[j]>=l[k]:
            l[j],l[k]=l[k],l[j]
print("the sorted list is:",l)