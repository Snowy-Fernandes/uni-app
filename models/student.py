from models.subject import Subject, get_grade

MAX_SUBJECTS = 4
PASS_MARK = 50


class Student:
    def __init__(self, student_id, name, email, password):
        self.id = student_id
        self.name = name
        self.email = email.lower()
        self.password = password
        self.subjects = []

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "subjects": [subject.to_dict() for subject in self.subjects],
        }

    @staticmethod
    def from_dict(data):
        student = Student(data["id"], data["name"], data["email"], data["password"])
        student.subjects = [Subject.from_dict(item) for item in data["subjects"]]
        return student

    def id_text(self):
        return f"{self.id:06d}"

    def can_enrol(self):
        return len(self.subjects) < MAX_SUBJECTS

    def enrol(self):
        if not self.can_enrol():
            return None
        taken_ids = [subject.id for subject in self.subjects]
        subject = Subject.make_new(taken_ids)
        self.subjects.append(subject)
        return subject

    def drop(self, subject_id):
        for subject in self.subjects:
            if subject.id == subject_id:
                self.subjects.remove(subject)
                return True
        return False

    def average_mark(self):
        if len(self.subjects) == 0:
            return 0
        total = sum(subject.mark for subject in self.subjects)
        return total / len(self.subjects)

    def grade(self):
        return get_grade(self.average_mark())

    def has_passed(self):
        return self.average_mark() >= PASS_MARK
