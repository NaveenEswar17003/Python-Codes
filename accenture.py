a = "Helloworld"

count = len(a)
print(count)  

countl = 0
for i in range(len(a)):
    if a[i] == "l":
        countl += 1

print(countl)  
