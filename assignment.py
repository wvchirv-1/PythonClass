#A python program that checks whether a number is an even number or odd number

number = int(input("Enter a number: "))

#check if the number is odd or even
if number % 2 == 0:
    print(f"{number} is an  even number.")


else:
    print(f"{number} is an odd number.")



#A python program that checks whether a letter is a vowel or consonant

letter = input("Enter a letter: ")
 #check if a vowel or consonant

if len(letter) == 1 and letter.isalpha():
    if letter in "aeiou" :
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant. ")

else:
    print("invalid input. Please enter a single letter.")

#Apthon program that returns the perimeter of a rectangle

length = float(input("enter the length of a rectangle: "))
width = float(input("enter the width of a rectangle"))


#calculate the perimeter
perimeter = 2 * (length +width)

#results
print(f"the perimeter of the rectangle is {perimeter}")

