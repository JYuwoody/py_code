# It create by chatgpt
import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents, Person

@pytest.fixture
def classroom():
    teacher = Teacher("Severus Snape")
    students = [Student("Harry Potter"), Student("Hermione Granger")]
    course_title = "Potions"
    return Classroom(teacher, students, course_title)

def test_add_student(classroom):
    classroom.add_student(Student("Ron Weasley"))
    assert len(classroom.students) == 3

def test_add_student_too_many(classroom):
    with pytest.raises(TooManyStudents):
        for _ in range(11):
            classroom.add_student(Student("Some Student"))

def test_remove_student(classroom):
    classroom.remove_student("Harry Potter")
    assert len(classroom.students) == 1

def test_change_teacher(classroom):
    classroom.change_teacher(Teacher("Minerva McGonagall"))
    assert classroom.teacher.name == "Minerva McGonagall"

def test_teacher_inherits_from_person():
    teacher = Teacher("Albus Dumbledore")
    assert isinstance(teacher, Person)

def test_student_inherits_from_person():
    student = Student("Draco Malfoy")
    assert isinstance(student, Person)
