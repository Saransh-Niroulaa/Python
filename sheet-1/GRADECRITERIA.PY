percentage = float(input("Enter the percentage: "))

if percentage < 0 or percentage > 100:
    print("Invalid percentage! Please enter a value between 0 and 100.")
else:
    if percentage < 25:
        grade = 'D'
    elif 25 <= percentage < 45:
        grade = 'C'
    elif 45 <= percentage < 65:
        grade = 'B'
    elif 65 <= percentage < 85:
        grade = 'A'
    else:
        grade = 'A+'
    print(f"Your grade is: {grade}")
