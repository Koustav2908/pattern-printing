rows = int(input("How many number of rows? "))
num_stars = 1

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("*" * num_stars)
    num_stars += 2
