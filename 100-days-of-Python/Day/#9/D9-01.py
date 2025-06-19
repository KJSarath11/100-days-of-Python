#grading program using dictionary
student_scores={
    "Alice":95,
    "Bob":87,
    "Charlie":62,
    "David": 76,
    "Eve":100
}

student_grades={}
#keepinf it empty since we will be adding the grades into this later on.

for student in student_scores:
    score=student_scores[student]
    if score>90:
        student_grades[student]="A"
    elif score>80:
        student_grades[student]="B"
    elif score>70:
        student_grades[student]="C"
    else:
        student_grades[student]="Fail"
  
print(student_grades)

