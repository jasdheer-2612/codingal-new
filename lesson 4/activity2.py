row = int(input('enter the number rows:'))

for i in range(row):
    for j in range(i+1):
        print('&', end='')
    print('')