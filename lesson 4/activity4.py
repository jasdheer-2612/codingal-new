num = int(input("enter the number: "))
flag = True
if num == 1:
    print(num, "is neither prime nor composite")
else:
    for i in range(2, num):

        if num % i == 0:
           flag = False
           break

    if flag == True:
        print(num, "is a prime number")
    else:
       print(num, "is not a prime number")
