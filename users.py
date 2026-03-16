from student_features import Student_features

class User:

    def __init__(self,user_id,password,role):
        self.user_id=user_id
        self.password=password
        self.role=role


    def verify_login(self,entered_id,entered_pwd):

        # checking with userinput and our object data

        return self.user_id == entered_id and self.password == entered_pwd

class Principal(User):

    def __init__(self, user_id, password):
        #role must always be "principal"
        super().__init__(user_id, password, "principal") # assigning the value principal to the role beacuse it is fixed for principal class

    def dashboard(self):
        print("Principal Dashboard")
        print("View student progress")
        print("View teacher reports")


class Teacher(User):

    def __init__(self, user_id, password):
        super().__init__(user_id, password, "teacher")

    def dashboard(self):
        print("""Teacher Dashboard\n
        1 View Timetable
        2 Mark Attendance
        3 Update Marks
        4 Update Remarks
        5 Logout""")

class Student(User):

    def __init__(self, user_id, password,student_class):
        super().__init__(user_id, password, "student")
        self.student_class=student_class

    def dashboard(self):

        print("""\nStudent Dashboard
            1 View Timetable
            2 View Marks
            3 View Attendance
            4 View Remarks
            5 Logout""")


class Parent(User,Student_features):

    def __init__(self, user_id, password,child_id):
        super().__init__(user_id, password, "parent")
        Student_features.__init__(self)
        self.child_id=child_id


    def dashboard(self):
        print("""Parent Dashboard
            1 View child marks
            2 View child attendance
            3 View child Remarks
            4 Logout""")









    






