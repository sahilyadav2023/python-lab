n=int(input("enter the no of elements:"))
l=list()
sum=0
product=1
for i in range(n):
    l.append(int(input("enter a number:")))
max=l[0]
for b in l:
    sum=sum+b
for c in l:
    product=product*b
for d in l:
    if max<d:
        max=d
print("the sum of list is ",sum)
print("the product of list is ",product)
print("the largest no of the list is ",max)