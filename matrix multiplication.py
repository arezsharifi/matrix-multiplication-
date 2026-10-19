c = []
a = [[1, 2, 3],[1, 2, 3]]                        # a is the first matrix
b = [[1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1]]

a1 = len(a)         # satr hay a 2
b1 = len(b[0])         # soton hay b 4
c1 = len(a[0])      # soton hay a 3
for i in range(a1):
    c.append([] * i)
    for j in range(b1):              ### it made a list to carry values
        c[i].append(0 * j)

for i in range(a1):
    for j in range(b1):
        for k in range(c1):
            c[i][j] += a[i][k] * b[k][j]


print(c)

