a = input("Enter the string : ")

l = list(a)

for i in range(len(l)) :
    if l[i] == 'a' or l[i] == 'e' or l[i] == 'i' or l[i] == 'o' or l[i] == 'u' :
        l[i] = "*"
print(l)