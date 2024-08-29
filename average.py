def main():
    grades = []  # Create an empty list to store the grades
    
    while True:
        grade_str = input("Enter a grade (or 'done' to finish): ")
        
        if grade_str.lower() == 'done':
            break  # Exit the loop if user enters 'done'
        
        try:
            grade = float(grade_str)  # Try to convert input to a number
            grades.append(grade)      # Add the grade to the list
        except ValueError:
            print("Please enter a valid number.")
    
    if grades:
        average = sum(grades) / len(grades)  # Calculate the average
        print(f"\nThe grades entered are: {grades}")
        print(f"The average grade is: {average:.2f}")
    else:
        print("No grades were entered.")

if __name__ == "__main__":
    main()
