rows = 8
for i in range(0, rows):
    for j in range(0, i + 1):
        print('*', end=" ")
    print("\r")

rows = 8
num = rows
# reverse for loop
for i in range(rows + 1, 0, -1):
    for j in range(0, i):
        print('*', end=' ')
    print("\r")