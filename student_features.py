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
    def view_timetable(self, class_section):

        timetable = self.data.timetable.get(class_section)

        if not timetable:
            print("Timetable not available")
            return

        teachers = self.data.teachers

        days = list(timetable.keys())
        max_periods = max(len(p) for p in timetable.values())

        # Header
        table_data = [["Day"] + [f"P{i+1}" for i in range(max_periods)]]

        # Rows
        for day in days:
            row = [day]

            for entry in timetable[day]:
                subject = entry["subject"]
                teacher_id = entry["teacher_id"]

                teacher_name = teachers.get(teacher_id, {}).get("name", "")

                row.append(f"{subject}\n({teacher_name})")

            # Fill empty cells if any
            while len(row) < max_periods + 1:
                row.append("")

            table_data.append(row)

        # Plot table
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.axis('off')

        table = ax.table(
            cellText=table_data,
            loc='center',
            cellLoc='center'
        )

        table.scale(1, 2)

        plt.title(f"Timetable - {class_section}")
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

    
    def compare_attendance(self):

        import matplotlib.pyplot as plt

        students = []
        percentages = []

        for student_id, data in self.data.attendance.items():
            total = data["total_classes"]
            attended = data["attended"]

            if total > 0:
                percent = (attended / total) * 100
            else:
                percent = 0

            students.append(student_id)
            percentages.append(percent)

        plt.figure()
        plt.bar(students, percentages)
        plt.title("Attendance Comparison")
        plt.xlabel("Students")
        plt.ylabel("Percentage")
        plt.show()
    
    def view_attendance(self, student_id):

        print("\nStudent Attendance\n")

        if student_id in self.data.attendance:

            total = self.data.attendance[student_id]["total_classes"]
            attended = self.data.attendance[student_id]["attended"]
            absent = total - attended

            percentage = (attended / total) * 100 if total > 0 else 0

            print("Total Classes :", total)
            print("Attended      :", attended)
            print("Absent        :", absent)
            print("Percentage    :", round(percentage, 2), "%")

            import matplotlib.pyplot as plt

            # Data
            labels = ["Present", "Absent"]
            values = [attended, absent]

            # Pie chart
            plt.figure()
            wedges, texts, autotexts = plt.pie(
                values,
                labels=labels,
                autopct='%1.1f%%',
                startangle=90
            )

            # Add legend (explains colors clearly)
            plt.legend(
                wedges,
                [f"Present ({attended})", f"Absent ({absent})"],
                title="Attendance",
                loc="best",
                bbox_to_anchor=(0.5,1.15)
            )

            plt.title(f"Attendance Distribution - {student_id}")

            plt.show()

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

            
