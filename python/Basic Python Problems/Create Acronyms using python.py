# we are going to create acronyms using python

# For example if the input is "ramesh prasath" then the output will be "RP"

userinput = str(input("Enter the phrase: "))

# for splitting the user input
var = userinput.split()

# var2 is to store acronym of phrase
var2 = " "

for i in var:
    var2 = var2 + str(i[0]).upper()
print(var2)