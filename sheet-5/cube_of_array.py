A = list(map(int, input("Enter array: ").split()))
B = []

for num in A:
    B.append(num * num * num)

print(B)
