import os
import json
import random

from models.student import Student

FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "students.data")


class Database:
    def __init__(self, file_path=FILE_PATH):
        self.file_path = file_path
        self.check_file()

    def check_file(self):
        if not os.path.exists(self.file_path):
            self.write_all([])

    def read_all(self):
        self.check_file()
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return [Student.from_dict(item) for item in json.load(file)]
        except (ValueError, KeyError, TypeError):
            return []

    def write_all(self, students):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump([student.to_dict() for student in students], file, indent=2)

    def add(self, student):
        students = self.read_all()
        students.append(student)
        self.write_all(students)

    def update(self, student):
        students = self.read_all()
        for index in range(len(students)):
            if students[index].id == student.id:
                students[index] = student
        self.write_all(students)

    def find_by_email(self, email):
        for student in self.read_all():
            if student.email.lower() == email.lower():
                return student
        return None

    def find_by_id(self, student_id):
        for student in self.read_all():
            if student.id == student_id:
                return student
        return None

    def find_login(self, email, password):
        for student in self.read_all():
            if student.email.lower() == email.lower() and student.password == password:
                return student
        return None

    def remove(self, student_id):
        students = self.read_all()
        kept = [student for student in students if student.id != student_id]
        self.write_all(kept)
        return len(kept) != len(students)

    def clear(self):
        self.write_all([])

    def new_student_id(self):
        taken_ids = [student.id for student in self.read_all()]
        new_id = random.randint(1, 999999)
        while new_id in taken_ids:
            new_id = random.randint(1, 999999)
        return new_id
