students = [
    {"name": "Alice", "math": 85, "science": 90, "history": 88},
    {"name": "Bob", "math": 75, "science": 80, "history": 78},
    {"name": "Charlie", "math": 90, "science": 82, "history": 92},
    {"name": "David", "math": 80, "science": 88, "history": 85},
    {"name": "Eve", "math": 92, "science": 78, "history": 90},
    {"name": "Frank", "math": 87, "science": 85, "history": 80},
    {"name": "Grace", "math": 33, "science": 51, "history": 20},  # Below average
    {"name": "Hannah", "math": 76, "science": 79, "history": 84},
    {"name": "Ivy", "math": 88, "science": 91, "history": 87},
    {"name": "Jack", "math": 40, "science": 39, "history": 35},  # Below average
    {"name": "Kevin", "math": 78, "science": 74, "history": 77},
    {"name": "Lily", "math": 95, "science": 89, "history": 94},  # Outstanding
    {"name": "Mason", "math": 79, "science": 81, "history": 83},
    {"name": "Nina", "math": 83, "science": 88, "history": 86},
    {"name": "Oscar", "math": 25, "science": 30, "history": 20},  # Below average
    {"name": "Penny", "math": 85, "science": 90, "history": 82},
    {"name": "Quinn", "math": 86, "science": 87, "history": 90},
    {"name": "Rachel", "math": 89, "science": 82, "history": 88},
    {"name": "Sam", "math": 81, "science": 84, "history": 83},
    {"name": "Tina", "math": 75, "science": 77, "history": 76},
    {"name": "Uma", "math": 94, "science": 93, "history": 95},  # Outstanding
    {"name": "Victor", "math": 80, "science": 82, "history": 81},
    {"name": "Wendy", "math": 77, "science": 79, "history": 78},
    {"name": "Xander", "math": 84, "science": 85, "history": 87},
    {"name": "Yara", "math": 91, "science": 90, "history": 92},  # Outstanding
    {"name": "Zane", "math": 79, "science": 81, "history": 84},
    {"name": "Aaron", "math": 86, "science": 88, "history": 85},
    {"name": "Beth", "math": 80, "science": 83, "history": 80},
    {"name": "Cody", "math": 75, "science": 79, "history": 76},
    {"name": "Dana", "math": 87, "science": 85, "history": 88},
    {"name": "Ella", "math": 92, "science": 89, "history": 91},  # Outstanding
    {"name": "Finn", "math": 79, "science": 80, "history": 82},
    {"name": "Gina", "math": 85, "science": 87, "history": 90},
    {"name": "Harry", "math": 81, "science": 83, "history": 82},
    {"name": "Isla", "math": 89, "science": 91, "history": 87},
    {"name": "Jake", "math": 45, "science": 38, "history": 40},  # Below average
    {"name": "Kara", "math": 88, "science": 90, "history": 89},
    {"name": "Liam", "math": 83, "science": 84, "history": 85},
    {"name": "Maya", "math": 92, "science": 93, "history": 94},  # Outstanding
    {"name": "Noah", "math": 90, "science": 87, "history": 89},
    {"name": "Owen", "math": 80, "science": 81, "history": 83},
    {"name": "Paige", "math": 85, "science": 88, "history": 86},
    {"name": "Quincy", "math": 77, "science": 75, "history": 78},
    {"name": "Rita", "math": 82, "science": 84, "history": 83},
    {"name": "Sean", "math": 89, "science": 91, "history": 92},  # Outstanding
    {"name": "Tara", "math": 84, "science": 85, "history": 88},
    {"name": "Ursula", "math": 91, "science": 89, "history": 90},
    {"name": "Vince", "math": 79, "science": 81, "history": 80},
    {"name": "Willa", "math": 88, "science": 87, "history": 90},
    {"name": "Xavier", "math": 83, "science": 82, "history": 84}
]


# Function to calculate average score for a subject
def average_score(subject):
    total = sum(student[subject] for student in students)
    return total / len(students)

def print_average_scores():
    for subject in ["math", "science", "history"]:
        print(f"Average {subject.capitalize()} Score: {average_score(subject):.2f}")

# Function to find student with the highest score in a subject
def highest_score(subject):
    highest = max(students, key=lambda x: x[subject])
    return highest["name"], highest[subject]

def print_highest_scores():
    for subject in ["math", "science", "history"]:
        name, score = highest_score(subject)
        print(f"Highest {subject.capitalize()} Score: {name} with {score}")

# Function to find student with the lowest score in a subject
def lowest_score(subject):
    lowest = min(students, key=lambda x: x[subject])
    return lowest["name"], lowest[subject]

def print_lowest_scores():
    for subject in ["math", "science", "history"]:
        name, score = lowest_score(subject)
        print(f"Lowest {subject.capitalize()} Score: {name} with {score}")

# Function to calculate the total score for each student
def calculate_total_score(student):
    return student['math'] + student['science'] + student['history']

# Add total score and rank to each student
for student in students:
    student['total'] = calculate_total_score(student)

# Sort students by total score in descending order to determine rank
students_sorted_by_total = sorted(students, key=lambda x: x['total'], reverse=True)

for rank, student in enumerate(students_sorted_by_total, start=1):
    student['rank'] = rank

def print_student_ranks():
    print("\nStudent Rankings:")
    for student in students_sorted_by_total:
        print(f"Rank {student['rank']}: {student['name']} with total {student['total']}")

# Function to identify failing students
def failing_students():
    return [student['name'] for student in students if min(student['math'], student['science'], student['history']) < 40]

def print_failing_students():
    fails = failing_students()
    print(f"Failing Students: {', '.join(fails) if fails else 'None'}")

# Function to identify students who didn't give an exam (score recorded as None)
def students_missing_exam():
    return [student['name'] for student in students if None in (student['math'], student['science'], student['history'])]

def print_students_missing_exam():
    missing = students_missing_exam()
    print(f"Students Missing an Exam: {', '.join(missing) if missing else 'None'}")

# Function to calculate percentage score for each student
def calculate_percentage(student):
    total_possible = 300  # Assuming each subject is out of 100
    return (student['total'] / total_possible) * 100

def print_student_percentages():
    for student in students_sorted_by_total:
        print(f"{student['name']}: {calculate_percentage(student):.2f}%")

# Function to get the top N students based on total score
def top_n_students(n):
    return students_sorted_by_total[:n]

def print_top_n_students(n=5):
    top_students = top_n_students(n)
    print(f"\nTop {n} Students:")
    for student in top_students:
        print(f"{student['name']} with total {student['total']}")

# Function to identify students who have improved or declined in any subject
def performance_change():
    improvement = []
    decline = []
    
    for student in students:
        math_vs_science = student['math'] - student['science']
        science_vs_history = student['science'] - student['history']
        
        if math_vs_science > 0 and science_vs_history > 0:
            improvement.append(student['name'])
        elif math_vs_science < 0 and science_vs_history < 0:
            decline.append(student['name'])
    
    return improvement, decline

def print_performance_changes():
    improvement, decline = performance_change()
    print(f"Students with improvement: {', '.join(improvement) if improvement else 'None'}")
    print(f"Students with decline: {', '.join(decline) if decline else 'None'}")

# Function to analyze subject-wise distribution (e.g., number of students scoring in various ranges)
def subject_distribution(subject):
    ranges = {
        '90-100': 0,
        '80-89': 0,
        '70-79': 0,
        '60-69': 0,
        '50-59': 0,
        '40-49': 0,
        'Below 40': 0
    }
    
    for student in students:
        score = student[subject]
        if score >= 90:
            ranges['90-100'] += 1
        elif score >= 80:
            ranges['80-89'] += 1
        elif score >= 70:
            ranges['70-79'] += 1
        elif score >= 60:
            ranges['60-69'] += 1
        elif score >= 50:
            ranges['50-59'] += 1
        elif score >= 40:
            ranges['40-49'] += 1
        else:
            ranges['Below 40'] += 1
    
    return ranges

def print_subject_distribution():
    for subject in ["math", "science", "history"]:
        distribution = subject_distribution(subject)
        print(f"\n{subject.capitalize()} Score Distribution:")
        for range_name, count in distribution.items():
            print(f"{range_name}: {count} students")

# Function to identify the most and least consistent students based on the variance in their scores across subjects
def consistency_analysis():
    def variance(scores):
        mean = sum(scores) / len(scores)
        return sum((x - mean) ** 2 for x in scores) / len(scores)

    consistency = []
    
    for student in students:
        scores = [student['math'], student['science'], student['history']]
        var = variance(scores)
        consistency.append((student['name'], var))
    
    # Sort by variance
    consistency_sorted = sorted(consistency, key=lambda x: x[1])
    
    most_consistent = consistency_sorted[0]
    least_consistent = consistency_sorted[-1]
    
    return most_consistent, least_consistent

def print_consistency_analysis():
    most_consistent, least_consistent = consistency_analysis()
    print(f"Most Consistent Student: {most_consistent[0]} with variance {most_consistent[1]:.2f}")
    print(f"Least Consistent Student: {least_consistent[0]} with variance {least_consistent[1]:.2f}")

# Analysis options
switch_case = {
    1: print_average_scores,
    2: print_highest_scores,
    3: print_lowest_scores,
    4: print_student_ranks,
    5: print_failing_students,
    6: print_students_missing_exam,
    7: print_student_percentages,
    8: lambda: print_top_n_students(5),  # Example with n=5
    9: print_performance_changes,
    10: print_subject_distribution,
    11: print_consistency_analysis
}

# Example usage:
def main():
    while True:
        print("\nChoose an option:")
        print("1. Print Average Scores")
        print("2. Print Highest Scores")
        print("3. Print Lowest Scores")
        print("4. Print Student Ranks")
        print("5. Print Failing Students")
        print("6. Print Students Missing an Exam")
        print("7. Print Student Percentages")
        print("8. Print Top N Students")
        print("9. Print Performance Changes")
        print("10. Print Subject-wise Distribution")
        print("11. Print Consistency Analysis")
        print("0. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        if choice == 0:
            print("Exiting...")
            break
        elif choice in switch_case:
            switch_case[choice]()  # Call the appropriate function
        else:
            print("Invalid choice, please try again.")

if _name_ == "_main_":
    main()
    




