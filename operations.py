"""
1) Add the project title.
   a) Use a comment to label the program as "School Class Organiser".

2) Create a list of classmates.
   a) Store student names inside a list.
   b) Print the full class list.

3) Access list values.
   a) Use `len()` to find the total number of students.
   b) Use index `0` to print the first student.
   c) Use index `-1` to print the last student.
   d) Use slicing to print the first three students.

4) Modify the list.
   a) Use `append()` to add a new student.
   b) Use `remove()` to delete a student.
   c) Use `sort()` to arrange names alphabetically.
   d) Use `reverse()` to reverse the list order.

5) Create a teacher dictionary.
   a) Store teacher details using key-value pairs.
   b) Add name, subject, and experience.

6) Perform dictionary operations.
   a) Access the subject using its key.
   b) Use `get()` to safely access experience.
   c) Update the experience value.
   d) Add an email key.
   e) Use `pop()` to remove experience.

7) Create a student directory.
   a) Create one list for roll numbers.
   b) Create one list for student names.
   c) Use `zip()` to pair roll numbers with names.
   d) Convert the pairs into a dictionary using `dict()`.

8) Access a student from the directory.
   a) Use the roll number key to print the student name.
"""

# 1) "School Class Organiser"

classmates = ["Shivam", "Dakshita", "Rohit", "Aarav", "Priya"]
print(classmates)

print("Total number of students: ", len(classmates))
print("First student: ", classmates[0])
print("Last student: ", classmates[-1])
print("First three students", classmates[:3])

classmates.append("Yug")
print ("Updated class list: ", classmates)
classmates.remove("Rohit")
print ("Updated class list after removing Rohit: ", classmates)
classmates.sort()
print ("Class list sorted alphabetically: ", classmates)
classmates.reverse()
print ("Class list reversed: ", classmates)

teacher = {"name": "Mrs. Rupinder Kaur", "subject": "Coding", "experience": 100}
print("Teacher's details: ", teacher)
print("Teacher's subject: ", teacher["subject"])
print("Teacher's experience: ", teacher.get("experience"))
teacher["experience"] = 200
print("Updated teacher's experience: ", teacher["experience"])
teacher["email"] = "rupinder.kaur@gmail.com"
print("Teacher's email: ", teacher["email"])
pop = teacher.pop("experience")

roll_numbers = [1, 2, 3, 4, 5]
zip_pairs = zip(roll_numbers, classmates)
print("Zip pairs: ", dict(zip_pairs))

