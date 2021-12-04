print("Welcome to the date-to-day converter/leap year checker.")
input_value = input("Enter any date in the format DDMMYYYY(after 1 Jan 1792 for accurate result). ")

# limitation on input value and user error detection-1
try:
    while len(input_value) != 8 or int(input_value[2:4]) > 12 or int(input_value[2:4]) < 1 or \
     int(input_value[0:2]) > 31 or int(input_value[0:2]) <= 0 or int(input_value) < 0:
        print("This date cannot be calculated. Please try again and check if the date is valid.")
        input_value = input("Enter any date in the form DDMMYYYY(after 1 jan 1792) ")
        print("\n")
except Exception as e:
    print("This date cannot be calculated. Please try again and check if the date is valid.")
    input_value = input("Enter any date in the form DDMMYYYY(after 1 jan 1792) ")
    print("\n")

# leap year check code
if int(input_value[4:]) % 4 == 0:
    if int(input_value[4:]) % 100 == 0 & int(input_value[4:]) % 400 != 0:
        leap_year = False
    elif int(input_value[4:]) % 400 == 0:
        leap_year = True
    else:
        leap_year = True
else:
    leap_year = False

# disclaimer for possibility of incorrect result
    if int(input_value[4:]) < 1752:
        print("The output day may not be accurate as the Gregorian calendar was not used at the time of the entered "
              "date.")

# start of date-to-day converter code
if leap_year:
    if int(input_value[2:4]) == 1:
        leap_year_anomaly = -1
    elif int(input_value[2:4]) == 2:
        leap_year_anomaly = -1
    else:
        leap_year_anomaly = 0
else:
    leap_year_anomaly = 0

month_code = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
century_code = [6, 4, 2, 0]
day_code = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

month_code_value = month_code[int(input_value[2:4])-1]
century_code_value = century_code[int(input_value[4:6]) % 4]
year_code_value = int(input_value[6:])
leap_year_value = int(input_value[6:])//4
date_value = int(input_value[:2])

final_result_code = (year_code_value + leap_year_value + century_code_value + month_code_value + date_value) % 7
final_result_day = day_code[final_result_code]

# final result output
print("The day on the date- " + input_value + " is a " + final_result_day)

if leap_year:
    print("This is also a leap year")
else:
    print("This is also not a leap year")