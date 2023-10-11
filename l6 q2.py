n = int(input('enter a number'))
sum = 0
count = 1
if n<1:
    print("invalid")
else:
    while count<=n:
        sum = sum +(1/count)
        count+=1
print(f'{sum:.9f}')
