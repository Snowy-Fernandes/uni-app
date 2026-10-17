from models.student import Student, MAX_SUBJECTS
from utils.console import say, ask, CYAN, GREEN, RED, YELLOW
from utils.validation import is_valid_email, is_valid_password


class StudentController:
    def __init__(self, db):
        self.db = db

    def run(self):
        while True:
            choice = ask("Student System (l/r/x): ", CYAN, 1).lower()
            if choice == "l":
                self.login()
            elif choice == "r":
                self.register()
            elif choice == "x":
                break

    def get_email_and_password(self):
        while True:
            email = ask("Email: ", "", 1)
            password = ask("Password: ", "", 1)
            if is_valid_email(email) and is_valid_password(password):
                say("email and password formats acceptable", YELLOW, 1)
                return email, password
            say("Incorrect email or password format", RED, 1)

    def register(self):
        say("Student Sign Up", GREEN, 1)
        email, password = self.get_email_and_password()

        old_student = self.db.find_by_email(email)
        if old_student is not None:
            say(f"Student {old_student.name} already exists", RED, 1)
            return

        name = ask("Name: ", "", 1)
        student = Student(self.db.new_student_id(), name, email, password)
        self.db.add(student)
        say(f"Enrolling Student {name}", YELLOW, 1)

    def login(self):
        say("Student Sign In", GREEN, 1)
        email, password = self.get_email_and_password()

        student = self.db.find_login(email, password)
        if student is None:
            say("Student does not exist", RED, 1)
            return
        self.course_menu(student)

    def course_menu(self, student):
        while True:
            choice = ask("Student Course Menu (c/e/r/s/x): ", CYAN, 2).lower()
            if choice == "c":
                self.change_password(student)
            elif choice == "e":
                self.enrol(student)
            elif choice == "r":
                self.remove_subject(student)
            elif choice == "s":
                self.show_subjects(student)
            elif choice == "x":
                break

    def change_password(self, student):
        say("Updating Password", YELLOW, 2)
        new_password = ask("New Password: ", "", 2)
        while not is_valid_password(new_password):
            say("Incorrect password format", RED, 2)
            new_password = ask("New Password: ", "", 2)

        confirm = ask("Confirm Password: ", "", 2)
        while confirm != new_password:
            say("Password does not match - try again", RED, 2)
            confirm = ask("Confirm Password: ", "", 2)

        student.password = new_password
        self.db.update(student)

    def enrol(self, student):
        subject = student.enrol()
        if subject is None:
            say(f"Students are allowed to enrol in {MAX_SUBJECTS} subjects only", RED, 2)
            return
        self.db.update(student)
        say(f"Enrolling in Subject-{subject.id}", YELLOW, 2)
        say(f"You are now enrolled in {len(student.subjects)} out of {MAX_SUBJECTS} subjects", YELLOW, 2)

    def remove_subject(self, student):
        text = ask("Remove Subject by ID: ", "", 2)
        if not text.isdigit() or not student.drop(int(text)):
            say(f"Subject {text} does not exist", RED, 2)
            return
        self.db.update(student)
        say(f"Dropping Subject-{int(text)}", YELLOW, 2)
        say(f"You are now enrolled in {len(student.subjects)} out of {MAX_SUBJECTS} subjects", YELLOW, 2)

    def show_subjects(self, student):
        say(f"Showing {len(student.subjects)} subjects", YELLOW, 2)
        for subject in student.subjects:
            say(str(subject), "", 2)
