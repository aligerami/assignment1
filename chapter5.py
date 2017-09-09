number_of_student=int(input("enter number of student"))


student1 = 0
score1 = 0
student2 = 0
score2 = 0

for i in range (0,number_of_student):
    student = input("Enter a student name: ")
    score = eval(input("Enter a student score: ")) 

    if score > score1:
        score2=score1
        student2=student1
        student1 = student
        score1 = score
    elif score>score2 :
        student2=student
        score2=score
        
print("First Highest Score student name is ",student1, " with score",score1)
print("Second Highest Score student name is ",student2, " with score",score2)