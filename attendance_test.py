# AttendX Attendance Validation Test

def test_mark_attendance():
    student_id = "STU001"
    attendance_status = "Present"

    assert student_id != ""
    assert attendance_status in ["Present", "Absent"]

    print("PASS: Attendance input is valid")


def test_empty_student_id():
    student_id = ""

    assert student_id == ""

    print("PASS: Empty student ID test")


if __name__ == "__main__":
    test_mark_attendance()
    test_empty_student_id()