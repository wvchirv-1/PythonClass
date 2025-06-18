#program1
age = int (input("how old are you"))

if age > 18 :
    print("you are a voter")

else:
    print("you are not a voter")



#progam2

temperature = float(input("enter current room temperature e.g 23.0"))

if temperature >25.0:
    print("it is too hot")

elif temperature <25.0:
    print("it is too cold")

else:
    print("normal temperature")


#program3
first = int (input("enter first number: "))
second = int (input("enter second number: "))
third = int (input("enter third number: "))


if first>second and first>third:
    print(first, "is the largest number")


elif second>first and second>third:
    print(second,"is the largest number")


else:
    print(third, "is the largest number")



