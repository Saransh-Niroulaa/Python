A = int(input("Enter a number: "))
original = A
reverse = 0

while A > 0:
    digit = A % 10
    reverse = reverse * 10 + digit
    A //= 10

if reverse == original:
    print("Yes")
else:
    print("No")
