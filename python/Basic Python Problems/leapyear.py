#### program to find the given year is leap year or not

year = input("Enter the year to check whether it is leap year or not : ")

if (int(year) % 400 == 0):
    print(year," is leap year")
elif (int(year) % 100 == 0):
    print(year," is not a leap year")
elif (int(year) % 4 == 0):
    print(year,"is leap year")
else:
    print(year,"is not a leap year")
