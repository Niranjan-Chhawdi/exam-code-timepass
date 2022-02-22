n = input("Enter the string : ")
y = n
h = len(n)
k = ''

for i in range (h - 1 , -1 , -1) :
    print(n[i] , end = " ")
    k = k + n[i]
    
if y == k :
    print("\n palindorome")
else :
    print("\n not")