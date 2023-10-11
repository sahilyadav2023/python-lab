n=int(input("enter a number"))
x=int(input("enter a number"))
if n<0 or x<0:
    print("enter a positive number")
else:
    sum =1 
    for i in range(1,n+1):
        sum = sum + ((x**i)/i)
        
    print(f'{sum:9f}')
    
