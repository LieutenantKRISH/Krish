if __name__ == '__main__':
    students = []
    for i in range(int(input(""))):
        name = input("")
        score = float(input(""))
        students.append([name, score])

    students.sort(key=lambda x: x[1])
    second_lowest_score = None
    second_lowest_students = []

    for j in range(1, len(students)):
        if students[j][1] > students[0][1]:
            second_lowest_score = students[j][1]
            break

    for student in students:
        if student[1] == second_lowest_score:
            second_lowest_students.append(student[0])

    second_lowest_students.sort()

    for n in second_lowest_students:
        print(n)
EXPLANATION:-

(1)  if __name__ == '__main__'::
This line checks if the code is being run as the main program and not imported as a module. 
It ensures that the following code block will only execute if the file is being run directly.


(2)  students = []:
This line initializes an empty list called students to store the names and scores of the students.
(3)  for i in range(int(input(""))):
This line prompts the user to enter the number of students and converts it to an integer using int().
The range() function creates a loop that runs the specified number of times.

(4)  name = input(""):
This line prompts the user to enter the name of each student and assigns it to the variable name.

(5)  score = float(input("")):
This line prompts the user to enter the score of each student and converts it to a float using float().
The score is assigned to the variable score.
(6)  students.append([name, score]):
This line adds a sublist containing the student's name and score ([name, score]) to the students list.

(7)  students.sort(key=lambda x: x[1]):
This line sorts the students list based on the scores in ascending order.
The key parameter specifies the sorting criterion, where lambda x: x[1] indicates that the sorting should be based on 
the second element (the score) of each sublist.

(8)  second_lowest_score = None:
This line initializes a variable second_lowest_score to store the second lowest score.
It is initially set to None to indicate that no second lowest score has been found yet.

(9)  second_lowest_students = []:
This line initializes an empty list second_lowest_students to store the names of students with the second lowest score.

(10)  for j in range(1, len(students)):
This line creates a loop that iterates over the students list, starting from the second student (index 1) until the end.
It uses the variable j to represent the index.

(11)  if students[j][1] > students[0][1]:
This line checks if the score of the current student, students[j][1], is greater than the score of the first student, students[0][1].
If the condition is true, it means that the current score is different from the highest score, so it assigns the second lowest score 
to second_lowest_score and breaks the loop.

(12)  for student in students:
This line creates a loop that iterates over each student sublist in the students list.
The variable student represents each sublist.

(13)  if student[1] == second_lowest_score:
This line checks if the score of the current student, student[1], is equal to the second_lowest_score.
If the condition is true, it means the student has the second lowest score.

(14)  second_lowest_students.append(student[0]):
This line adds the name of the current student, student[0], to the second_lowest_students list.
It collects the names of students with the second lowest score.

(15)  second_lowest_students.sort():
This line sorts the second_lowest_students list alphabetically.

(16)  for n in second_lowest_students::
This line creates a loop that iterates over each name in the second_lowest_students list.
The variable n represents each name.

(17)  print(n):
This line prints each name on a new line.
It prints the names of students with the second lowest score, which were stored in the second_lowest_students list.
