#while loop

number = 20

while number <=25 :
    print(number)
    number += 1


#decrementing
count = 105
while count >=100:
    print("number is",count)
    count -=1


#break and continue
a = 20
while a <=25:
    print(a)
    if a == 23:
        break
    a +=1


counter = 35
while counter >=40:
    if counter ==37:
        counter +=1
    print(counter)
    counter +=1






#for loop
languages = ["python , C++ , Java , PHP"]
for lang in languages:
    print(lang)


for num in range(5):
    print(num)

for x in range(10, 15):
    print(x)

for z in range(10, 20, 3):
    print(z)