A = list(map(int, input("Enter array: ").split()))
B = int(input("Enter element to search: "))

found = 0
for num in A:
    if num == B:
        found = 1
        break

print(found)
