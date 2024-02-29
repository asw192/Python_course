class Student:
       
    students_list = []
    
    def __init__(self, name, age, grades):
        """
        Initialize the student with name, age, and grades.
        """
        self.name = name
        self.age = age
        self.grades = grades  # Assuming grades is a list of numbers
        
        # Add this instance to the students list
        Student.students_list.append(self)
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}")
    
    @staticmethod
    def calculate_average_grade(student):
        if student.grades:
            return sum(student.grades) / len(student.grades)
        else:
            return 0
    
    @classmethod
    def calculate_class_average(cls):
        total_average = 0
        for student in cls.students_list:
            total_average += cls.calculate_average_grade(student)
        if cls.students_list:
            return total_average / len(cls.students_list)
        else:
            return 0

# Create some student instances
student1 = Student("John Doe", 20, [88, 92, 85])
student2 = Student("Jane Smith", 22, [91, 90, 93])

# Display individual student information
student1.display_info()
student2.display_info()

# Calculate and print the average grade of a single student
print(f"Average grade of {student1.name}: {Student.calculate_average_grade(student1)}")

# Calculate and print the class average grade
print(f"Class average grade: {Student.calculate_class_average()}")
