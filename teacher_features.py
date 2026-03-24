import json
# from student_features import DATA_PATH
from utils.file_handling import load_data,save_data
from utils.data_manager import DataManager



class TeacherFeatures:

    def __init__(self):

        # with open(DATA_PATH + "marks.json","r") as file:
        #     self.marks=json.load(file)

        # with open(DATA_PATH + "attendance.json","r") as file:
        #     self.attendance=json.load(file)

        # self.marks=load_data("marks.json")
        # self.attendance=load_data("attendance.json")
        self.data=DataManager()

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

        while True:
            status=input("enter the attendance (p/a): ")

            if status not in ["p","a"]:
                print("Invalid input! Enter only 'p' or 'a'")
                continue

            break

        if student_id not in self.data.attendance:
            self.data.attendance[student_id]={
                "total_classes":0,
                "attended":0
            }

        self.data.attendance[student_id]["total_classes"]+=1

        if status.lower()=="p":
            self.data.attendance[student_id]["attended"]+=1

            # with open(DATA_PATH + "attendance.json","w") as file:
            #     json.dump(self.attendance,file,indent=4)

            self.data.save_all()

        print("Attendance updated successfully")





    
    def update_marks(self,student_id,exam):

        subjects = ["Math", "Physics", "English"]
        subject_marks={}

        for subject in subjects:
            while True:

                try:

                    mark=int(input(f"enter {subject} marks: "))
                    if mark < 0 or mark > 100:
                        print("Marks should be between 0 and 100")
                        continue

                    break
                except ValueError:
                    print("Invalid input! Enter a number.")
            subject_marks[subject]=mark

        if student_id not in self.data.marks:
            self.data.marks[student_id]={}

        self.data.marks[student_id][exam]=subject_marks

        # with open(DATA_PATH + "marks.json","w") as file:
        #     json.dump(self.marks,file,indent=4)

        # Save using DataManager
        self.data.save_all()

        print("Marks updated successfully")


    def update_remarks(self,student_id):


        while True:
            remark = input("Enter remark for student: ")

            if remark == "":
                print("Remark can not be empty")
                continue
            break


        # with open("remarks.json","r") as file:

        #     remarks=json.load(file)
        #self.data.load_data()
        if student_id not in self.data.remarks:
            self.data.remarks[student_id]=[]

        

        self.data.remarks[student_id].append(remark)
        
        # with open(DATA_PATH + "remarks.json","w") as file:
        #     json.dump(remarks,file,indent=4)

        self.data.save_all()
        
        print("Remark updated successfully")
