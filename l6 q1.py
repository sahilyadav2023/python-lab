n = str(input('enter the sentence '))
v= 'aeiou'
s = ' '
l= len(n)
vow = 0
cons = 0
words = 1
for char in n:
    if char in v:
        vow+=1
    elif char in s:
        words+=1
    else:
        cons+=1
print(vow)
print(cons)
print(words)
         
    