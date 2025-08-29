num = int(input("Enter a number: "))

if num % 7 == 0 or num % 10 == 5:
    print(f"{num} is either divisible by 7 or has last digit as 5")
else:
    print(f"{num} is neither divisible by 7 nor has last digit as 5")