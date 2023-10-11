a=int(input("enter no of rows:"))
b=int(input("enter no of columns:"))
c=int(input("enter no of rows in 2:"))
d=int(input("enter no of columns in 2:"))
mat1=[]
mat2 = []
mat3=[]
for i in range(a):
    mat1.append([ ]) 
    for j in range(b):
        mat1[i].append(int(input("enter matrix elements")))
for i in range(c):
    mat2.append([ ])
    for _ in range(d):
        mat2[i].append(int(input("enter matrix elements")))
for i in range(c):
    mat3.append([])
    for j in range(d):
        mat3=mat1[i][j]+mat2[i][j]
print(mat1)
print(mat2)
print(mat3)

