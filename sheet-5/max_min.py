A = list(map(int, input("Enter array: ").split()))

maximum = A[0]
minimum = A[0]

for num in A:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print(maximum, minimum)
