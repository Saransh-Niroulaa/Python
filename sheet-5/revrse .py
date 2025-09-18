A = list(map(int, input("Enter array: ").split()))
rev = []

for i in range(len(A)-1, -1, -1):
    rev.append(A[i])

print(rev)
