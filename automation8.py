str1= input('enter a sentence :')
str2 =[]
for e in str1:
    if e not in str2:
        str2.append(e)

for s in str2:
    print(s,':',str1.count(s))