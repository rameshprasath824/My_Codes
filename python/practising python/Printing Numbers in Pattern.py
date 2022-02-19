# In this file we are printing numbers in pattern

# Taking input
totalrows = int(input("Enter total number of row: "))

# Printing numbers in increasing left sided triangle

for row in range(1, totalrows + 1):
    for number in range(1, row + 1):
        print(f"{number}", end="")
    print()
print()  # for space

# Printing numbers in increasing right sided triangle

for row in range(1, totalrows + 1):
    # printing spaces
    for space in range(1, (totalrows - row) + 1):
        print(" ", end="")

    # printing number
    for number in range(1, row + 1):
        print(f"{number}", end="")
    print()
print()  # for space

# Printing numbers in decreasing triangle order

for row in range(0, totalrows + 1):
    for number in range(1, (totalrows - row) + 1):
        print(f"{number}", end="")
    print()

# Printing full size triangle

for row in range(1, totalrows + 1):
    # printing spaces
    for space in range(1, (totalrows - row) + 1):
        print(" ", end="")
    # printing numbers
    for number in range(1, row + 1):
        print(f"{number}", end="")

    for secondary in range(1, row):
        print(f"{secondary + row}", end="")
    print()
