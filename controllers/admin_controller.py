from utils.console import say, ask, CYAN, RED, YELLOW

GRADE_ORDER = ["Z", "P", "C", "D", "HD"]


def student_line(student):
    return f"{student.name} :: {student.id_text()} --> GRADE: {student.grade():>2} - MARK: {student.average_mark():.2f}"


class AdminController:
    def __init__(self, db):
        self.db = db

    def run(self):
        while True:
            choice = ask("Admin System (c/g/p/r/s/x): ", CYAN, 1).lower()
            if choice == "c":
                self.clear_all()
            elif choice == "g":
                self.group_by_grade()
            elif choice == "p":
                self.partition_pass_fail()
            elif choice == "r":
                self.remove_student()
            elif choice == "s":
                self.show_students()
            elif choice == "x":
                break

    def show_students(self):
        say("Student List", YELLOW, 1)
        students = self.db.read_all()
        if len(students) == 0:
            say("< Nothing to Display >", "", 2)
        for student in students:
            say(f"{student.name} :: {student.id_text()} --> Email: {student.email}", "", 1)

    def group_by_grade(self):
        say("Grade Grouping", YELLOW, 1)
        students = self.db.read_all()
        if len(students) == 0:
            say("< Nothing to Display >", "", 2)
            return
        for grade in GRADE_ORDER:
            group = [student_line(s) for s in students if s.grade() == grade]
            if group:
                say(f"{grade:<2} --> [{', '.join(group)}]", "", 1)

    def partition_pass_fail(self):
        say("PASS/FAIL Partition", YELLOW, 1)
        students = self.db.read_all()
        failed = [student_line(s) for s in students if not s.has_passed()]
        passed = [student_line(s) for s in students if s.has_passed()]
        say(f"FAIL --> [{', '.join(failed)}]", "", 1)
        say(f"PASS --> [{', '.join(passed)}]", "", 1)

    def remove_student(self):
        text = ask("Remove by ID: ", "", 1)
        if text.isdigit() and self.db.remove(int(text)):
            say(f"Removing Student {text} Account", YELLOW, 1)
        else:
            say(f"Student {text} does not exist", RED, 1)

    def clear_all(self):
        say("Clearing students database", YELLOW, 1)
        answer = ask("Are you sure you want to clear the database (Y)ES/(N)O: ", RED, 1).upper()
        if answer == "Y":
            self.db.clear()
            say("Students data cleared", YELLOW, 1)
