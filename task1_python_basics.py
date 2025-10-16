# Project 1 - Task 1: Python Data Structures & Control Flow
# Student: Teona Berozashvili
# Honor Code: i certify that this work is my own and i have not plagiarized

students = {
    "S001": {"name": "Itachi Uchiha", "scores": [95, 92, 88, 90], "attendance": 28},
    "S002": {"name": "Kisame Hoshigaki", "scores": [78, 81, 74, 80], "attendance": 26},
    "S003": {"name": "Pain (Nagato)", "scores": [90, 94, 96, 92], "attendance": 30},
    "S004": {"name": "Konan", "scores": [85, 89, 83, 88], "attendance": 29},
    "S005": {"name": "Deidara", "scores": [76, 72, 70, 74], "attendance": 24},
    "S006": {"name": "Sasori", "scores": [82, 79, 85, 80], "attendance": 27},
    "S007": {"name": "Hidan", "scores": [55, 60, 58, 62], "attendance": 20},
    "S008": {"name": "Kakuzu", "scores": [88, 84, 91, 87], "attendance": 28},
    "S009": {"name": "Tobi (Obito)", "scores": [93, 96, 94, 98], "attendance": 30},
    "S010": {"name": "Zetsu", "scores": [64, 67, 59, 70], "attendance": 22},
}


# total number of classes 
total_classes=30


#function 1: calculate average score
def calculate_average(scores: list) -> float:
    return round(sum(scores)/len(scores),2)


#function 2: assign letter grade 
def assign_grade(average: float) -> str:
    if average>=90:
        return "A"
    elif average>=80:
        return "B"
    elif average>=70:
        return "C"
    elif average>=60:
        return "D"
    else:
        return "F"


#function 3: check if student passes 
def check_eligibility(student_dict: dict, total_classes: int) -> tuple:
    scores=student_dict["scores"]
    attendance=student_dict["attendance"]
    average=calculate_average(scores)
    attendance_rate=(attendance/ total_classes)*100

    if average >=60 and attendance_rate >=75:
        return (True,"Passed")
    elif average <60:
        return (False,"Low average")
    else:
        return (False,"Low attendance")


#function 4:find top n students by average 
def find_top_performers(students: dict, n: int) -> list:
   # helper function to get average from tuple (id, avg)
    def get_average(item):
        return item[1]

    averages = []

    #go through every student
    for student_id, info in students.items():
        avg = calculate_average(info["scores"])
        averages.append((student_id, avg))

    
    sorted_students = sorted(averages, key=get_average, reverse=True)
    return sorted_students[:n]



#function 5:generate overall course report 
def generate_report(students: dict) -> dict:
    total_students=len(students)
    passed=0
    failed=0
    all_scores=[]
    total_attendance=0

    for student in students.values():
        avg = calculate_average(student["scores"])
        passed_flag, _ =check_eligibility(student, total_classes)
        if passed_flag:
            passed += 1
        else:
            failed += 1
        all_scores.extend(student["scores"])
        total_attendance+=student["attendance"]

    class_average=round(sum(all_scores) / len(all_scores), 2)
    highest_score=max(all_scores)
    lowest_score=min(all_scores)
    avg_attendance=round((total_attendance/(total_students * total_classes))* 100, 2)

    return {
        "total_students":total_students,
        "passed":passed,
        "failed":failed,
        "class_average":class_average,
        "highest_score":highest_score,
        "lowest_score":lowest_score,
        "average_attendance_rate":avg_attendance,
    }



if __name__ == "__main__":
    report = generate_report(students)
    top_students = find_top_performers(students, 5)

    print("=== COURSE STATISTICS ===")
    print(f"Total Students: {report['total_students']}")
    print(f"Passed: {report['passed']} ({round((report['passed']/report['total_students'])*100, 2)}%)")
    print(f"Failed: {report['failed']} ({round((report['failed']/report['total_students'])*100, 2)}%)")
    print(f"Class Average: {report['class_average']}")
    print(f"Average Attendance Rate: {report['average_attendance_rate']}%")
    print()

    print("=== TOP 5 PERFORMERS ===")
    for i, (sid, avg) in enumerate(top_students, start=1):
        grade = assign_grade(avg)
        print(f"{i}. {sid} - {students[sid]['name']}: {avg} ({grade})")
    print()

    print("=== STUDENTS WHO FAILED ===")
    for sid, info in students.items():
        passed,reason =check_eligibility(info, total_classes)
        if not passed:
            avg = calculate_average(info["scores"])
            print(f"{sid} - {info['name']}: {reason} ({avg})")
    
   
    print()
    print("=== GRADE DISTRIBUTION ===")

    grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for info in students.values():
        avg= calculate_average(info["scores"])
        grade= assign_grade(avg)
        grade_distribution[grade]+= 1

    for grade,count in grade_distribution.items():
        print(f"{grade}: {count} students")
