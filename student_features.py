import json
from utils.file_handling import save_data,load_data
from utils.data_manager import DataManager
import matplotlib.pyplot as plt


# def load_timetable():
#     with open("data/timetable.json","r") as file:
#         return json.load(file)






# DATA_PATH="data/"
class Student_features:

    def __init__(self):
        

        # self.timetable={
        #     7: {
        #         "Monday": ["Math", "Physics", "English"],
        #         "Tuesday": ["Chemistry", "Math", "Social"],
        #         "Wednesday": ["Biology", "Math", "English"],
        #         "Thursday": ["Physics", "Chemistry", "Math"],
        #         "Friday": ["English", "Social", "Math"]
        #     }
        # }

       

        # with open(DATA_PATH + "marks.json","r") as file:
        #     self.marks=json.load(file)

        # with open(DATA_PATH + "attendance.json","r") as file:
        #     self.attendance=json.load(file)

        # with open( DATA_PATH + "remarks.json","r") as file:
        #     self.remarks=json.load(file)

        # self.marks=load_data("marks.json")
        # self.attendance=load_data("attendance.json")
        # self.remarks=load_data("remarks.json")

        # object of DataManager
        self.data=DataManager()

    def view_timetable(self, student_class):

        #data= load_timetable()
        timetable = self.data.timetable.get("students", {}).get(str(student_class), {})

        if not timetable:
            print("Timetable not available")
            return

        days = list(timetable.keys())
        periods = len(timetable[days[0]])

        table_data = [["Day"] + [f"P{i+1}" for i in range(periods)]]

        for day in days:
            table_data.append([day] + timetable[day])

        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.axis('off')

        table = ax.table(cellText=table_data, loc='center', cellLoc='center')
        table.scale(1, 2)

        plt.title(f"Class {student_class} Timetable")
        plt.show()
        
        





    def view_marks(self,student_id):

        print("Student marks\n")

        if student_id in self.data.marks:

            exams=self.data.marks[student_id]

            for exam,subjects in exams.items():
                print(exam + " Exam")

            
                for subject,mark in subjects.items():

                    print(subject, ":", mark)

                print()
        else:
            print("marks not available")

    
    def view_attendance(self,student_id):

        print("Student Attendance\n")

        if student_id in self.data.attendance:

            total=self.data.attendance[student_id]["total_classes"]
            attended=self.data.attendance[student_id]["attended"]

            percentage=(attended/total)*100

            print("Total Classes :", total)
            print("Attended      :", attended)
            print("Percentage    :", round(percentage, 2), "%")

        else:

            print("Attendance data not available")

    def view_remarks(self,student_id):
        print("\nStudent Remarks\n")
        if student_id in self.data.remarks:
            remarks=self.data.remarks[student_id]

            if not remarks:
                print("No remarks available.")
            else:
                for i,remark in enumerate(remarks,start=1):
                    print(f"{i}. {remark}")
        else:

            print("Remarks not available")

            
