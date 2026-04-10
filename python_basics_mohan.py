#Task 1

person_name = "krishna"

age = 20

height = 160.0

is_student = True


#Task 2
print(f"person_name:{person_name} | age:{age}| height:{height} | is_student:{is_student} ")


#Task 3
age_in_months = 20*12

age_in_days = 20*365

Remainder = 20 // 7

age_power = 20**2

print(f"age_in_months:{age_in_months} | age_in_days:{age_in_days} | Remainder:{Remainder} | age_power:{age_power}")



#Assignment: Python Functions and Lists You are building a simple marks analysis utility.Complete the following tasks in order. 
Task 1. Write a function calculate_total(marks) that accepts a list of marks and returns their sum. 
Task 2. Write a function calculate_average(marks) that calls calculate_total() and returns the average. 
Task 3. Write a function get_grade(average) that returns "A" if average > 90, "B" if average > 75, and "C" otherwise.
Task 4. Write a function display_report(marks) that calls all three functions above and prints: Total: <value> Average: <value> Grade: <value>
Task 5. Add a docstring to each function describing what it does. Test your solution with the list [88, 76, 95, 60, 82].

def calculate_total(marks):
    """Takes a list of marks and returns their sum."""
    return sum(marks)

def calculate_average(marks):
    """Calculates average by calling calculate_total() function."""
    if not marks: return 0
    total = calculate_total(marks)
    return total / len(marks)

def get_grade(average):
    """Returns "A" if average > 90, "B" > 75, else "C"."""
    if average > 90:
        return "A"
    elif average > 75:
        return "B"
    else:
        return "C"

def display_report(marks):
    """Displays total, average, and grade for the given marks."""
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = get_grade(average)
    
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

# Test the solution
test_marks = [88, 76, 95, 60, 82]
display_report(test_marks)
