import json



class TeacherFeatures:

    def __init__(self):

        with open("marks.json","r") as file:
            self.marks=json.load(file)

        with open("attendance.json","r") as file:
            self.attendance=json.load(file)

    def view_timetable(self):

        timetable={

        "Monday": ["Class 7 - Math"],
        "Tuesday": ["Class 7 - Physics"],
        "Wednesday": ["Class 7 - Math"],
        "Thursday": ["Class 7 - Physics"],
        "Friday": ["Class 7 - Math"]

        }

        for day,classes in timetable.items():
            print(day, ":", ", ".join(classes))

    
    def update_attendance(self,student_id):

        status=input("enter the attendance (p/a): ")

        if student_id not in self.attendance:
            self.attendance[student_id]={
                "total_classes":0,
                "attended":0
            }

        self.attendance[student_id]["total_classes"]+=1

        if status.lower()=="p":
            self.attendance[student_id]["attended"]+=1

        with open("attendance.json","w") as file:
            json.dump(self.attendance,file,indent=4)

        print("Attendance updated successfully")





    
    def update_marks(self,student_id,exam):

        subjects = ["Math", "Physics", "English"]
        subject_marks={}

        for subject in subjects:

            mark=int(input(f"enter {subject} marks: "))
            subject_marks[subject]=mark

        if student_id not in self.marks:
            self.marks[student_id]={}

        self.marks[student_id][exam]=subject_marks

        with open("marks.json","w") as file:
            json.dump(self.marks,file,indent=4)

        print("Marks updated successfully")


    def update_remarks(self,student_id):
        remark = input("Enter remark for student: ")

        with open("remarks.json","r") as file:

            remarks=json.load(file)
        

        remarks[student_id]=remark

        with open("remarks.json","w") as file:
            json.dump(remarks,file,indent=4)
        
        print("Remark updated successfully")
