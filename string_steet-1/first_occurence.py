A = input()
B = int(input())

charfind = chr(B)

index = A.find(charfind)
if index != -1 :
    print(index)
else :
    print(-1)