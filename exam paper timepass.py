d = {"january" : 31 , "february" : 28 , "march" : 31 , "april" : 30 , "may" : 31 , "june" : 30 , "july" : 31 , "august" : 31 , "september" : 30 , "october" : 31 , "november" : 30 , "december" : 31}

a = input("Enter the Month name : ")
# first part
print("month and date ")
for i in d :
    if i == a :
        print(d[i])

# second part
print("In alphabetical order")
print()
l = list(d.keys())
l.sort()
print(l)
print()

# third part
print("All month with 31 days")
print()
for i in d :
    if d[i] == 31 :
        print(i)
print()
# fourth part

print("Month according to number of days")
print("february")

for i in d :
    if d[i] == 30 :
        print(i)
for i in d :
    if d[i] == 31 :
        print(i)





