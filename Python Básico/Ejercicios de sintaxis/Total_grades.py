total_grades = int(input("How many grades do you want to average? "))
add=0
counter = 1
approved_grades = 0
failed_grades= 0
average_approved_grades = 0
average_failed_grades= 0
while(counter <=total_grades):
    print("Add grade number: ",counter)
    grade = float(input())
    add = add+grade
    counter = counter+1
    if (grade >= 70):
        approved_grades = approved_grades + 1
        average_approved_grades = average_approved_grades + grade
    else:
        failed_grades = failed_grades+1
        average_failed_grades = average_failed_grades + grade
if(approved_grades > 0):
    average_approved_grades = average_approved_grades /approved_grades
else:
    print("There are no approved grades")
if(failed_grades > 0):
    average_failed_grades = average_failed_grades / failed_grades
else:
    print("There are no failed grades")
total_average = add / total_grades
print("The total of approved grades is", approved_grades)
print("The average of approved grades is", average_approved_grades)
print("The total of failed grades is", failed_grades)
print("The average of failed grades is", average_failed_grades)
print("The total grade average grades is", total_average)