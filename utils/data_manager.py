import json
from utils.file_handling import save_data,load_data

class DataManager:

    def __init__(self):
        self.marks=load_data("marks.json")
        self.remarks=load_data("remarks.json")
        self.attendance=load_data("attendance.json")
        self.timetable=load_data("timetable.json")

    def save_all(self):
        save_data("marks.json", self.marks)
        save_data("remarks.json",self.remarks)
        save_data("attendance.json",self.attendance)
        save_data("timetable.json",self.timetable)
        