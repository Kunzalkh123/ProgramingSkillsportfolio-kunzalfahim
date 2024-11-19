#Exercise 5: Days of the Month
month_days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
days_month = int(input("Enter a month number (1-12): "))
if 1 <= days_month <= 12:
    print(f"The month {days_month} has {month_days[days_month]} days.")
else:
    print("Please enter a number between 1 and 12.")

#Advanced Requirement:
leap_year=input("Is it leap year?")
leap_year= "Yes"

if leap_year.lower() == leap_year.lower():
    print("2 has 29 days in leap year.")
else:
    print("2 has 28 days in non leap year")
