student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


#TODO-2: Write your code below to covert scores into grades.👇
#Hint: Use a for loop here. 

def convertGrades(scores: dict):
    for key in scores:
        grade = scores[key]
        letterGrade:str
        if grade >= 90:
            letterGrade = "A"
        elif grade <= 89 and grade > 79:
            letterGrade = "B"
        elif grade <= 79 and grade > 69:
            letterGrade = "C"
        elif grade <= 69 and grade > 59:
            letterGrade = "D"
        else:
            letterGrade = "F"
        student_grades[key] = letterGrade
        

#Don't change the code below 👇
convertGrades(student_scores)
print(student_grades)