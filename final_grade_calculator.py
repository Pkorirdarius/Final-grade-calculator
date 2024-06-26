# Initialize an empty list to store grades and set the final exam weight to 100
grades = []
final_exam_weight = 100

# Print a header for the final exam calculator
print("\n           ***Final Exam Calculator***\n")

# Define a function to input data with error handling
def input_function(datatype, user_input):
    while True:
        try:
            # Try to convert the input to the specified data type
            variable = datatype(input(user_input))
            return variable
        except ValueError:
            # If the input is invalid, print an error message and try again
            if datatype == int:
                print("\nERROR!Invalid input.\nPlease enter a whole number.\n")
            elif datatype == float:
                print("\nERROR!Invalid input.\nPlease enter a number.\n")

# Ask the user for the number of assessments (excluding the final exam)
assessment_count = input_function(int, "Enter the number of assessments (excluding final exam): ")

# Loop through each assessment
for assessment in range(assessment_count):
    print(f"\n       ***Assessment {assessment + 1}***")
    # Ask the user for the raw marks, total marks, and weight for each assessment
    score = input_function(float, f"\nEnter the raw marks for assessment {assessment + 1}: ")
    total_marks = input_function(float, "\nOut of: ")
    weight = input_function(float, "\nWeight(%): ")

    # Calculate the grade for each assessment and add it to the list
    grades.append(score/total_marks * weight)
    # Subtract the weight of each assessment to get the true weight of the final exam
    final_exam_weight -= weight

# Ask the user for their desired final grade
print("\n\n         ***Desired Grade***")
desired_grade = input_function(float, "\nDesired final grade (%): ")
desiredGrade = desired_grade

# Calculate the remaining grade needed to reach the desired grade
for grade in grades:
    desired_grade -= grade

# Calculate the final exam grade needed to reach the desired grade
final_exam = (desired_grade * 100)/final_exam_weight

# Print the result
if final_exam > 100:
    print(f"\n\n\n          :(Sorry mate!\n\nYou need to get {round(final_exam, 2)}% in the final exam to score {desiredGrade}% in this unit\n\nTry harder next time")
else:
    print(f"\n\n\n          :) WooHoo!!!\n\nYou just need to get {round(final_exam, 2)}% in the final exam to score {desiredGrade}% in this unit.\n\nYou got this!!!")