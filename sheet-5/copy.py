A = list(map(int, input("Enter array: ").split()))
B = int(input("Enter B: "))

new_arr = []
for x in A:
    new_arr.append(x + B)

print(new_arr)
