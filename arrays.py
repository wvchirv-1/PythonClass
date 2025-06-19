
courses =["FullStack","Datascience","cybersecurity"]
print(courses)

#Accessing an element
print(courses[2])

#Looping through an array
for course in courses:
    print(course)

#adding a new element
courses.append("UI/UX")
print(courses)


#Removing an element
courses.remove("Datascience")
print(courses)