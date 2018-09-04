n = int(input("Enter the length of the sequence: ")) # Do not change this line


n1 = 0
n2 = 0
n3 = 1
x = n1+n2+n3
counter = 0

while counter < n:
    print(x-n1)
    n1 = n2
    n2 = n3
    n3 = x
    x = n1+n2+n3
    counter = counter + 1
    



    


#klarad
