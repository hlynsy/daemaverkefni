top_num = int(input("Input a number between 0 and 999: "))

for i in range(0, top_num):
    if i < 10:
        i**1 == i
        print(i)
    elif i < 100:
        num1 = i // 10
        num2 = i % 10
        if ((num1**2) + (num2**2)) == i:
            print(i)
    elif i >= 100:
        num1 = i // 100
        num2and3 = i % 100
        num2 = num2and3 // 10
        num3 = num2and3 % 10
        if ((num1**3) + (num2**3) + (num3**3)) == i:
            print(i)