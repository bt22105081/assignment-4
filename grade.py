# program to print the grade given the marks

marks = int(input("enter the marks of the student "))
grade = ''
count = 0
if(marks > 80 and marks <=100):
    grade = 'A'
elif(60 < marks <=80):
    grade = 'B'
elif(50 < marks <=60):
    grade = 'C'
elif(45 < marks <=50):
    grade = 'D'
elif(25 < marks <=45):
    grade = 'E'
elif(0 < marks <=25):
    grade = 'F'
else:
    print("Wrong input of marks")
    count+=1
    
if (count == 0):
    print("The grade of the student with marks = ",marks," is ",grade)

