import json
# from student_features import DATA_PATH
from utils.file_handling import load_data,save_data
from utils.data_manager import DataManager
import matplotlib.pyplot as plt
import pandas as pd

# def load_timetable():
#     import json
#     with open("data/timetable.json", "r") as file:
#         return json.load(file)



class TeacherFeatures:

    def __init__(self):

        # with open(DATA_PATH + "marks.json","r") as file:
        #     self.marks=json.load(file)

        # with open(DATA_PATH + "attendance.json","r") as file:
        #     self.attendance=json.load(file)

        # self.marks=load_data("marks.json")
        # self.attendance=load_data("attendance.json")
        self.data=DataManager()

    def view_timetable(self, class_section):

        timetable = self.data.timetable.get(class_section)

        if not timetable:
            print("No timetable found")
            return

        teachers = self.data.teachers

        days = list(timetable.keys())

        # find max periods
        max_periods = max(len(timetable[day]) for day in days)

        table_data = []

        for day in days:
            row = []

            for entry in timetable[day]:
                subject = entry["subject"]
                teacher_id = entry["teacher_id"]

                # get teacher name
                teacher_name = teachers.get(teacher_id, {}).get("name", teacher_id)

                row.append(f"{subject}\n({teacher_name})")

            # fill empty cells
            while len(row) < max_periods:
                row.append("")

            table_data.append([day] + row)

        # column headers
        columns = ["Day"] + [f"P{i+1}" for i in range(max_periods)]

        df = pd.DataFrame(table_data, columns=columns)

        # display using matplotlib
        fig, ax = plt.subplots()
        ax.axis('off')

        table = ax.table(
            cellText=df.values,
            colLabels=df.columns,
            loc='center',
            cellLoc='center'
        )

        table.scale(1, 2)
        plt.title(f"Timetable - {class_section}")
        plt.show()
    def update_timetable(self, class_section):

        timetable = self.data.timetable.get(class_section)

        if not timetable:
            print("Timetable not available")
            return

        print("\nAvailable Days:")
        for day in timetable:
            print("-", day)

        day = input("Enter day to update: ").capitalize()

        if day not in timetable:
            print("Invalid day")
            return

        print("\nCurrent Periods:")
        for i, entry in enumerate(timetable[day], start=1):
            print(f"{i}. {entry['subject']} ({entry['teacher_id']})")

        # SAFE INPUT
        while True:
            try:
                period_index = int(input("Enter period number to change: ")) - 1
                if period_index < 0 or period_index >= len(timetable[day]):
                    print("Invalid period number!")
                    continue
                break
            except ValueError:
                print("Enter a number only!")

        new_subject = input("Enter new subject: ")
        new_teacher_id = input("Enter teacher ID: ")

        timetable[day][period_index] = {
            "subject": new_subject,
            "teacher_id": new_teacher_id
        }

        self.data.save_all()

        print("Timetable updated successfully!")

    def delete_timetable(self, class_section):

        timetable = self.data.timetable.get(class_section)

        if not timetable:
            print("No timetable found")
            return

        print("\nAvailable Days:")
        for day in timetable:
            print("-", day)

        day = input("Enter day: ").capitalize()

        if day not in timetable:
            print("Invalid day")
            return

        # Show periods
        print("\nCurrent Periods:")
        for i, entry in enumerate(timetable[day], start=1):
            print(f"{i}. {entry['subject']} ({entry['teacher_id']})")

        # Safe input
        while True:
            try:
                period_index = int(input("Enter period number to delete: ")) - 1

                if period_index < 0 or period_index >= len(timetable[day]):
                    print("Invalid period number!")
                    continue

                break
            except ValueError:
                print("Enter a number only!")

        # Delete specific period
        removed = timetable[day].pop(period_index)

        self.data.save_all()

        print(f"Deleted: {removed['subject']} successfully!")
        



    
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
