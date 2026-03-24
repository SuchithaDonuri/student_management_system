from users import Principal,Teacher,Student,Parent
from student_features import *
from teacher_features import *




principal = Principal("P101", "admin123")
teacher = Teacher("T201", "teach123")
student = Student("S301", "stud123",7)
parent = Parent("PA401", "parent123","S301")


#objects 
student_features=Student_features()
teacher_features=TeacherFeatures()




role=input("enter the role (principal/teacher/student/parent) : ")
user_id=input("enter the user id: ")
password=input("enter the password: ")


if role =="principal":

    if principal.verify_login(user_id,password):
        principal.dashboard()
        while True:
            

            choice=input("Enter you choice: ")

            if choice =="1":
                student_features.view_timetable(student.student_class)
            elif choice == "2":
                student_id=input("enter student id: ")
                student_features.view_marks(student_id)
            elif choice == "3":
                student_id=input("enter student id: ")
                student_features.view_attendance(student_id)
            elif choice == "4":
                student_id=input("enter student id: ")
                student_features.view_remarks(student_id)
            elif choice == "5":
                teacher_features.view_timetable()

            elif choice == "6":
                print("Logging out...")
                break

    else:
        print("Invalid credentials for principal")

elif role=="teacher":

    if teacher.verify_login(user_id,password):

        while True:
            teacher.dashboard()
            choice=input("Enter your choice: ")

            if choice=="1":
                teacher_features.view_timetable()

            elif choice=="2":
                student_id=input("enter student id: ")
                teacher_features.update_attendance(student_id)

            elif choice=="3":
                student_id=input("enter student id: ")
                exam=input("enter the exam (Quaterly/Half-Yearly/Annual): ")
                teacher_features.update_marks(student_id,exam)

            elif choice=="4":
                student_id=input("enter studend id: ")
                teacher_features.update_remarks(student_id)

            elif choice=="5":
                print("Logging out....")
                break
    

        
    else:
        print("Invalid teacher credentials")

elif role=="student":

    if student.verify_login(user_id,password):
        

        while True:
            student.dashboard()
            choice=input("Enter your choice: ")

            if choice=="1":

                student_features.view_timetable(student.student_class)

            elif choice == "2":
                
                student_features.view_marks(student.user_id)

                

            elif choice == "3":

                student_features.view_attendance(student.user_id)

            elif choice == "4":

                student_features.view_remarks(student.user_id)

            elif choice == "5":

                print("Logging out...")
                break

            else:

                print("Invalid choice")

    else:
        print("Invalid student credentials")

elif role=="parent":

    if parent.verify_login(user_id,password):
        while True:

            parent.dashboard()

            choice = input("Enter your choice: ")

            if choice=="1":
                student_id=input("enter studend id: ")
                parent.view_marks(parent.child_id)
            elif choice=="2":
                student_id=input("enter studend id: ")
                parent.view_attendance(parent.child_id)
            elif choice=="3":
                student_id=input("enter studend id: ")
                parent.view_remarks(parent.child_id)

            elif choice=="4":
                print("Logging out...")
                break

        


    else:
        print("Invalid parent credentials")

else:

    print("Invalid role")
    





