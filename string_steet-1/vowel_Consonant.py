t=  input()
v=0
c=0
for i in t:
    if i in 'aeiouAEIOU':
        v=v+1
    else:
        c=c+1
print("Vowels:",v)
print("Consonants:",c)