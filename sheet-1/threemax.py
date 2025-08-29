a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c

print("The maximum number is:", maximum)