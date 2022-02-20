# Here we will be printing different styles of hollow triangles

# taking input from user
totalrows = int(input("Enter the number of rows: "))

# Printing increasing left hollow triangle
for row in range(0, totalrows + 1):
    for column in range(0, totalrows + 1):
        if (column == 0) or (row == totalrows) or (row == column):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

# Printing increasing hollow triangle in reverse order
for row in range(0, totalrows + 1):
    for column in range(0, totalrows + 1):
        if (row == totalrows) or (column == totalrows) or (row + column == totalrows):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

# Printing decreasing hollow triangle
for row in range(0, totalrows + 1):
    for column in range(0, totalrows + 1):
        if (row == 0) or (column == totalrows) or (row == column):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

# Printing decreasing hollow triangle in reverse order
for row in range(0, totalrows + 1):
    for column in range(0, totalrows + 1):
        if (row == 0) or (column == 0) or (row + column == totalrows):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
