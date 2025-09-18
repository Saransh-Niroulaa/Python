A = list(map(int, input("Enter array: ").split()))

even_count = 0
odd_count = 0

for num in A:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if even_count > odd_count:
    print(even_count - odd_count)
else:
    print(odd_count - even_count)
