# We are going to calculate the age of the person by taking the date of birth as a input

# using datetime module
import datetime

# taking date of birth input from user
user_intput = input("Enter your date of birth in 'dd.mm.yyyy' format\n")

# checking the DOB format
def validate(date_of_birth):
    try:
        datetime.datetime.strptime(user_intput, '%d.%m.%Y')
    except:
        print("Enter your date of birth in correct format")
        exit()

validate(user_intput)

today_date = datetime.datetime.today()

date_of_birth = datetime.datetime.strptime(user_intput, '%d.%m.%Y')

age_temp_days = today_date - date_of_birth

total_days = age_temp_days.days

age_years = total_days / 365
age_months = total_days % 12
age_days =  total_days % 30

print(f"You are {int(age_years)} years, {int(age_months)} months and {int(age_days)} days old")
