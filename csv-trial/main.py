import csv


def get_students():
        with open("students.csv", "r") as students_file:
                student_records = csv.DictReader(students_file)
                
                students = []
                for student in student_records:
                        students.append(student)

        return students

def get_teachers():
        with open("teachers.csv", "r") as teachers_file:
                teacher_records = csv.DictReader(teachers_file)
                
                teachers = []
                for teacher in teacher_records:
                        teachers.append(teacher)

        return teachers


if __name__ == "__main__":
        with open("sample.txt", "w") as f:
                f.write("Student Name--> {}\n".format(get_students()))
                f.write("Teacher Name--> {}".format(get_teachers()))



with open("students.csv", "r") as students_file:
    student_records = csv.DictReader(students_file)

    with open("teachers.csv", "r") as teachers_file:
        teacher_records = csv.DictReader(teachers_file)

        for student in student_records:
            for teacher in teacher_records:

                # student_names = student["first_name"] + " " + student["last_name"]
                # teacher_names = teacher["first_name"] + " " +  teacher["last_name"]

                with open("new_names.csv", "w") as new_file:

                    csv_writer = csv.writer(new_file)
                    csv_writer.writerow(["Teacher Name", "Student Name"])
                        
                    csv_writer.writerow([teacher["first_name"], student["first_name"]])

