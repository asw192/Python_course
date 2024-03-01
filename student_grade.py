def input_grades():
    grades = {}
    while True:
        subject = input("Enter subject (or type 'done' to finish): ")
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter grade for {subject}: "))
            if grade < 0 or grade > 100:
                raise ValueError("Grade must be between 0 and 100.")
            grades[subject] = grade
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue
    return grades

def save_grades(grades, filename="grades.txt"):
    try:
        with open(filename, "a") as file:
            for subject, grade in grades.items():
                file.write(f"{subject},{grade}\n")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def read_and_calculate_average(filename="grades.txt"):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if not lines:
                return 0.0
            total_grade = 0
            for line in lines:
                subject, grade = line.strip().split(',')
                total_grade += float(grade)
            return total_grade / len(lines)
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
        return None
    except ValueError as e:
        print(f"An error occurred while processing the file: {e}")
        return None

def main():
    print("Grade Tracker")
    grades = input_grades()
    if grades:
        save_grades(grades)
        average_grade = read_and_calculate_average()
        if average_grade is not None:
            print(f"Your average grade is: {average_grade:.2f}")
        else:
            print("Could not calculate the average grade.")
    else:
        print("No grades were entered.")

if __name__ == "__main__":
    main()
