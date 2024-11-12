lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
x = []
y = []
for i in lis:
    if i not in x:
        x.append(i) 
for i in x:
    if lis.count(i) > 1:
        y.append(i)
print(y)
print(x)