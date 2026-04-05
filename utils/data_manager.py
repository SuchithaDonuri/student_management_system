import json
from utils.file_handling import save_data,load_data

class DataManager:

    def __init__(self):
        self.marks=load_data("marks.json")
        self.remarks=load_data("remarks.json")
        self.attendance=load_data("attendance.json")
        self.timetable=load_data("timetable.json")
        self.students=load_data("students.json")
        self.teachers=load_data("teachers.json")

    def save_all(self):
        save_data("marks.json", self.marks)
        save_data("remarks.json",self.remarks)
        save_data("attendance.json",self.attendance)
        save_data("timetable.json",self.timetable)
        save_data("students.json",self.students)
        save_data("teachers.json",self.teachers)
        
    def get_student(self,student_id):
        return self.students.get(student_id)
    
    def validate_student(self,student_id,dob):
        student=self.get_student(student_id)
        if student and student["dob"] == dob:
            return student
        return None
    
    def get_class_section(self,student_id):
        student=self.get_student(student_id)
        if student:
            return f"{student['class']}_{student['section']}"
        
        return None
    def get_timetable_by_student(self,student_id):
        class_section=self.get_class_section(student_id)
        if class_section:
            return self.timetable.get(class_section)
        return None
    
    