stars = int(input("Max number of stars: ")) # Do not change this line

#print stars 1 - n
for i in range(1, stars+1):
    for star in range(1, i+1):
        print("*", end="")
    print("")

#print stars from (n-1) to 1
for i in range((stars-1), 0, -1):
    for star in range(1, i+1):
        print("*", end="")
    print("")