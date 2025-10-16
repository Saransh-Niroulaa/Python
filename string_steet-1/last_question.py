s = input("enter the string: ")
s1 = s+s
print ("concatenated string is: " , s1)
print("---------------------------------------")
for i in s :
    if i.isupper() :
       s1 = s1.replace(i,"")
print("string after removing uppercase letters is: ", s1)
print("---------------------------------------")
for i in s :
    if i in "aeiouAEIOU" :
       s1 = s1.replace(i,"#")
print("string after replacing vowels with ""#"" is: ", s1)
print("---------------------------------------")

        