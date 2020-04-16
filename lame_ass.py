levels = 5
for i in range(levels):
    for j in range(levels - i - 1):
        print(' ',end='')
    for j in range(1 + i * 2):
        print('*',end='')
    print()
