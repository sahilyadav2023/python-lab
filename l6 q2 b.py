n = int(input('enter a number'))
sum = 0
a=1
fact= 1
while a<=n:
        fact=fact*a
        sum = sum +(1/fact)
        a+=1
print(f'{sum:.9f}')
