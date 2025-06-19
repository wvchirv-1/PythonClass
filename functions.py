#1. Built-functions/standard library functions

x = max(67, 89, 90, 23, 67, 45)
print("the maximum number is",x)

y = min(67, 89,90, 23, 67, 45)
print("the minimum number is",y)

z = pow(2, 3)
print("the power of 2 is",z)


#2. user-defined functions
def greeting():
    print("hello world!")

greeting() #calling a function


def school():
    print("My coding school is eMobilis")

school()


#paramiter and argument
def add(num1, num2):
    print(num1 + num2)

add(5, 10)
add(20, 10)


def student(fullname,course,gender):
    print(fullname,course,gender)

student("Abbie Wachira","MIT","Female")
student("John Kamau","MIT","male")
student("Mary Mbotela","MIT","Female")
student("Boaz Kariuki","MIT","male")


#Python program that displays details of five employees
#fintech using parameter and argument
#(fullname,email,age,position,salary,marriage status)



    # Function to display employee details
def display_employee(fullname, email, age, position, salary, marital_status):
        print("------ Employee Details ------")
        print(f"Full Name      : {fullname}")
        print(f"Email          : {email}")
        print(f"Age            : {age}")
        print(f"Position       : {position}")
        print(f"Salary         : KES {salary:,}")
        print(f"Marital Status : {marital_status}")
        print("------------------------------\n")

    # Calling the function for five employees
display_employee("Aria Wanjiru", "aria@wanjiru@gmail.com", 30, "Software Engineer", 15100.00, "Single")
display_employee("Brian Onyango", "brian@gmail.co.ke", 35, "Data Analyst", 11300.00, "Married")
display_employee("Cessy Mwende", "cessy@yahoo.com", 41, "Product Manager", 20000.00, "Married")
display_employee("Davis Kamau", "davie@yahoo.co.ke", 27, "UI/UX Designer", 1200.00, "Single")
display_employee("Esther Chelegat", "esther@yahoo.co.ke", 32, "Cybersecurity Analyst", 18000.00, "Divorced")









