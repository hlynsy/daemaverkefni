top_num = int(input("Upper number for the range: ")) # Do not change this line


for j in range(1,top_num):
    divisor = 0

    for i in range(1,j):
        if j % i == 0:
            divisor += i
    if divisor == j:
        print(j)
        