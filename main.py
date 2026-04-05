from users import Principal,Teacher,Student,Parent
from student_features import *
from teacher_features import *
from utils.data_manager import DataManager


data=DataManager()

principal = Principal("P101", "admin123")
# teacher = Teacher()
# student = Student("S301", "stud123",7)
parent = Parent("PA401", "parent123","S301")


#objects 
student_features=Student_features()
teacher_features=TeacherFeatures()



while True:
    role=input("enter the role (principal/teacher/student/parent) : ").lower()

    if role not in ["principal", "teacher", "student", "parent"]:
        print("Invalid role! Try again.")
        continue
    break



user_id=input("enter the user id: ")
password=input("enter the password: ")



if role =="principal":

    if principal.verify_login(user_id,password):
        while True:
            principal.dashboard()
        
            while True:
                try:
                    choice=int(input("Enter you choice: "))
                    if choice < 1 or choice > 6:
                        print("Invalid choice..Enter choice between 1 to 6 ")
                        continue
                    break
                except ValueError:
                    print("Enter numbers only!")

            if choice ==1:
                class_section = input("Enter class_section (e.g., 6_A): ").strip().replace(" ", "")
                if class_section not in data.timetable:
                    print("No timetable found for this class/section")
                else:
                    student_features.view_timetable(class_section)

                
                
                
            elif choice == 2:
                student_id=input("enter student id: ")
                student_features.view_marks(student_id)
            elif choice == 3:
                student_id=input("enter student id: ")
                student_features.view_attendance(student_id)
            elif choice == 4:
                student_id=input("enter student id: ")
                student_features.view_remarks(student_id)
            elif choice == 5:
                class_section = input("Enter class_section (e.g., 6_A): ").strip().replace(" ", "")
                if class_section not in data.timetable:
                    print("No timetable found for this class/section")
                else:
                    teacher_features.view_timetable(class_section)

            elif choice == 6:
                print("Logging out...")
                break

    else:
        print("Invalid credentials for principal")

elif role=="teacher":


    teachers=data.teachers.get(user_id)
    if teachers and teachers["password"] == password:
        teacher=Teacher(user_id,teachers["password"], teachers["teacher_type"],teachers["name"],teachers["subject"])        

        while True:
            teacher.dashboard()
            while True:
                
                try:
                    choice=int(input("Enter your choice: "))
                    if choice < 1 or choice > 7:
                        print("Invalid choice..Enter choice again")
                        continue
                    break
                except ValueError:
                    print("Enter numbers only!")

            if choice==1:
               
                class_section = input("Enter class_section (e.g., 6_A): ").strip()
                teacher_features.view_timetable(class_section)

            elif choice == 2:
                class_section = input("Enter class_section (e.g., 6_A): ").strip().replace(" ", "")
                teacher_features.update_timetable(class_section)

            elif choice == 3:
                class_section = input("Enter class_section (e.g., 6_A): ").strip().replace(" ", "")
                teacher_features.delete_timetable(class_section)

            elif choice==4:
                student_id=input("enter student id: ")
                teacher_features.update_attendance(student_id)

            elif choice==5:
                student_id=input("enter student id: ")
                exam=input("enter the exam (Quaterly/Half-Yearly/Annual): ")
                teacher_features.update_marks(student_id,exam)

            elif choice==6:
                student_id=input("enter studend id: ")
                teacher_features.update_remarks(student_id)

            elif choice==7:
                print("Logging out....")
                break


        
    else:
        print("Invalid teacher credentials")

elif role=="student":
    student_data=data.validate_student(user_id,password)

    if student_data:
        student=Student(user_id,student_data["class"],student_data["section"],student_data["name"])
        print(f""" =============== WELCOME {student.name} ================
Roll No : {student.user_id}
Class   : {student.student_class} (Section {student.section})
You are successfully logged in.""")

        while True:
            student.dashboard()

            while True:
                try:
                    choice=int(input("Enter your choice: "))
                    if choice < 1 or choice > 5:
                        print("Invalid choice..Enter choice again")
                        continue
                    break
                except ValueError:
                    print("Enter numbers only!")
            if choice == 1:
                key=student.get_class_section_key()
                student_features.view_timetable(key)
            elif choice == 2:
                student_features.view_marks(student.user_id)
            elif choice == 3:
                student_features.view_attendance(student.user_id)
            elif choice == 4:
                student_features.view_remarks(student.user_id)

            elif choice == 5:
                print("Logging out...")
                break
    else:
        print("Invalid student credentials")




elif role=="parent":

    if parent.verify_login(user_id,password):

        while True:
            parent.dashboard()


            # while loop for input validation
            while True:
                try:
                    choice=int(input("Enter your choice: "))
                    if choice < 1 or choice > 4:
                        print("Invalid choice..Enter choice again")
                        continue
                    break
                except ValueError:
                    print("Enter numbers only!")


            if choice==1:
                student_id=input("enter studend id: ")
                student_features.view_marks(student_id)
            elif choice==2:
                student_id=input("enter studend id: ")
                student_features.view_attendance(student_id)
            elif choice==3:
                student_id=input("enter studend id: ")
                student_features.view_remarks(student_id)

            elif choice==4:
                print("Logging out...")
                break

            


    else:
        print("Invalid parent credentials")

else:

    print("Invalid role")
    





