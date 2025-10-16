A= input()
B= A.split()
C= []
for i in B:
    C.append(i[::-1])
print(" ".join(C))
