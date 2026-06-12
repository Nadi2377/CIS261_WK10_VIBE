#Hanadi Hall    
#CIS261
#Wk10 VIBE Coding

"""
Student Grade Calculator Program
This program manages student records including test scores and calculates grades.
Uses a list of dictionaries to store student data.
"""

import os
from typing import List, Dict

# File to store student records
FILENAME = "student_grades.txt"


def calculate_average(test1: float, test2: float, test3: float) -> float:
    """Calculate average of three test scores."""
    return (test1 + test2 + test3) / 3


def get_letter_grade(average: float) -> str:
    """Determine letter grade based on average score."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def load_students() -> List[Dict]:
    """Load student records from file."""
    students = []
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split('|')
                        if len(parts) == 7:
                            student = {
                                'name': parts[0],
                                'id': parts[1],
                                'test1': float(parts[2]),
                                'test2': float(parts[3]),
                                'test3': float(parts[4]),
                                'average': float(parts[5]),
                                'grade': parts[6]
                            }
                            students.append(student)
            print(f"\n✓ Loaded {len(students)} student(s) from {FILENAME}")
        except Exception as e:
            print(f"\n✗ Error loading file: {e}")
    return students


def save_students(students: List[Dict]) -> None:
    """Save student records to file in pipe-delimited format."""
    try:
        with open(FILENAME, 'w') as file:
            for student in students:
                line = (f"{student['name']}|{student['id']}|"
                       f"{student['test1']:.2f}|{student['test2']:.2f}|"
                       f"{student['test3']:.2f}|{student['average']:.2f}|"
                       f"{student['grade']}\n")
                file.write(line)
        print(f"✓ Saved {len(students)} student(s) to {FILENAME}")
    except Exception as e:
        print(f"✗ Error saving file: {e}")


def add_student(students: List[Dict]) -> None:
    """Add a new student record."""
    print("\n" + "="*50)
    print("ADD NEW STUDENT")
    print("="*50)
    
    try:
        name = input("Enter student name: ").strip()
        if not name:
            print("✗ Name cannot be empty!")
            return
        
        student_id = input("Enter student ID: ").strip()
        if not student_id:
            print("✗ Student ID cannot be empty!")
            return
        
        # Get test scores with validation
        test1 = float(input("Enter Test 1 score (0-100): "))
        if not (0 <= test1 <= 100):
            print("✗ Test score must be between 0 and 100!")
            return
        
        test2 = float(input("Enter Test 2 score (0-100): "))
        if not (0 <= test2 <= 100):
            print("✗ Test score must be between 0 and 100!")
            return
        
        test3 = float(input("Enter Test 3 score (0-100): "))
        if not (0 <= test3 <= 100):
            print("✗ Test score must be between 0 and 100!")
            return
        
        # Calculate average and grade
        average = calculate_average(test1, test2, test3)
        grade = get_letter_grade(average)
        
        # Create student record
        student = {
            'name': name,
            'id': student_id,
            'test1': test1,
            'test2': test2,
            'test3': test3,
            'average': average,
            'grade': grade
        }
        
        students.append(student)
        print(f"\n✓ Student {name} added successfully!")
        print(f"  Average: {average:.2f}, Grade: {grade}")
        
    except ValueError:
        print("✗ Invalid input! Please enter valid numbers for test scores.")


def display_all_students(students: List[Dict]) -> None:
    """Display all students in a formatted table."""
    if not students:
        print("\n✗ No students in database!")
        return
    
    print("\n" + "="*100)
    print("STUDENT RECORDS")
    print("="*100)
    print(f"{'Name':<20} {'ID':<12} {'Test 1':<10} {'Test 2':<10} {'Test 3':<10} {'Average':<10} {'Grade':<8}")
    print("-"*100)
    
    for student in students:
        print(f"{student['name']:<20} {student['id']:<12} "
              f"{student['test1']:<10.2f} {student['test2']:<10.2f} "
              f"{student['test3']:<10.2f} {student['average']:<10.2f} {student['grade']:<8}")
    
    print("="*100)


def display_class_statistics(students: List[Dict]) -> None:
    """Display class statistics."""
    if not students:
        print("\n✗ No students in database!")
        return
    
    averages = [student['average'] for student in students]
    
    highest_avg = max(averages)
    lowest_avg = min(averages)
    class_avg = sum(averages) / len(averages)
    
    print("\n" + "="*50)
    print("CLASS STATISTICS")
    print("="*50)
    print(f"Number of students: {len(students)}")
    print(f"Highest average: {highest_avg:.2f}")
    print(f"Lowest average: {lowest_avg:.2f}")
    print(f"Class average: {class_avg:.2f}")
    print("="*50)


def search_student(students: List[Dict]) -> None:
    """Search for a student by name (case-insensitive)."""
    print("\n" + "="*50)
    print("SEARCH STUDENT")
    print("="*50)
    
    search_name = input("Enter student name to search: ").strip().lower()
    
    if not search_name:
        print("✗ Search name cannot be empty!")
        return
    
    found_students = [s for s in students if search_name in s['name'].lower()]
    
    if not found_students:
        print(f"✗ No student found with name containing '{search_name}'")
    else:
        print(f"\n✓ Found {len(found_students)} student(s):")
        print("-"*80)
        print(f"{'Name':<20} {'ID':<12} {'Test 1':<10} {'Test 2':<10} {'Test 3':<10} {'Average':<10} {'Grade':<8}")
        print("-"*80)
        for student in found_students:
            print(f"{student['name']:<20} {student['id']:<12} "
                  f"{student['test1']:<10.2f} {student['test2']:<10.2f} "
                  f"{student['test3']:<10.2f} {student['average']:<10.2f} {student['grade']:<8}")


def display_menu() -> None:
    """Display the main menu."""
    print("\n" + "="*50)
    print("STUDENT GRADE CALCULATOR")
    print("="*50)
    print("1. Add new student")
    print("2. Display all students")
    print("3. View class statistics")
    print("4. Search for a student")
    print("5. Save and exit (or press ESC)")
    print("="*50)


def main() -> None:
    """Main program loop."""
    students = load_students()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5) or ESC to exit: ").strip().lower()
        
        # Handle ESC key (user can type 'esc' or just press Ctrl+C)
        if choice == 'esc' or choice == chr(27):
            print("\nSaving data...")
            save_students(students)
            print("Goodbye!")
            break
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_all_students(students)
        elif choice == '3':
            display_class_statistics(students)
        elif choice == '4':
            search_student(students)
        elif choice == '5':
            print("\nSaving data...")
            save_students(students)
            print("Goodbye!")
            break
        else:
            print("✗ Invalid choice! Please enter 1-5 or ESC to exit.")


if __name__ == "__main__":
    main()

