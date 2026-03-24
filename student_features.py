import json
from utils.file_handling import save_data,load_data
from utils.data_manager import DataManager






DATA_PATH="data/"
class Student_features:

    def __init__(self):
        

        self.timetable={
            7: {
                "Monday": ["Math", "Physics", "English"],
                "Tuesday": ["Chemistry", "Math", "Social"],
                "Wednesday": ["Biology", "Math", "English"],
                "Thursday": ["Physics", "Chemistry", "Math"],
                "Friday": ["English", "Social", "Math"]
            }
        }

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

        print("Student Timetable\n")


        if student_class in self.timetable:

            for day, subjects in self.timetable[student_class].items():

                print(day, ":", ", ".join(subjects))
            print()

        else:
            print("Timetable not available")



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

            print(self.data.remarks[student_id])
        else:

            print("Remarks not available")

            