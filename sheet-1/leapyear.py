year = input("Enter a year: ")


if not year.isdigit():
    print("Please enter a valid number")
else:
    year = int(year)
    if year <= 0:
        print("Please enter a positive year")
    elif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
