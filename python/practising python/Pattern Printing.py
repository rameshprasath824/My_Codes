# In this file we will be printing different kinds of patter printing using stars

# Printing left oriented increasing triangle stars

n = 5
for i in range(n):
    for j in range(0, i+1):
        print("*", end="")  # here end = "" will print the values in single line
    print()  # this statement will print the values in next line for every New iteration
print()  # this statement is for space between two pattern outputs

# Printing Right oriented increasing triangle

for i in range(1, n + 1):
    for j in range(1,(n - i)+1):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()
print()

# Printing left oriented decreasing triangle stars

for i in range(1, n):
    for j in range(0, n - i):
        print("*", end="")
    print()
print()

# Printing full Triangle

for i in range(n):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    for l in range(i + 1):
        print("*", end="")

    print()
