A = list(map(int, input("Enter array: ").split()))

odd = []
even = []

for num in A:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

for x in odd:
    print(x, end=" ")
print()
for x in even:
    print(x, end=" ")
