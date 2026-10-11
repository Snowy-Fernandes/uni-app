import random


def get_grade(mark):
    if mark < 50:
        return "Z"
    if mark < 65:
        return "P"
    if mark < 75:
        return "C"
    if mark < 85:
        return "D"
    return "HD"


class Subject:
    def __init__(self, subject_id, mark):
        self.id = subject_id
        self.mark = mark
        self.grade = get_grade(mark)

    @staticmethod
    def make_new(taken_ids):
        new_id = random.randint(1, 999)
        while new_id in taken_ids:
            new_id = random.randint(1, 999)
        mark = random.randint(25, 100)
        return Subject(new_id, mark)

    def to_dict(self):
        return {"id": self.id, "mark": self.mark}

    @staticmethod
    def from_dict(data):
        return Subject(data["id"], data["mark"])

    def __str__(self):
        return f"[ Subject::{self.id:03d} -- mark = {self.mark} -- grade = {self.grade:>3} ]"
