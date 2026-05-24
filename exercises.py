# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()


# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    letter = input("Please enter a letter (a-z or A-Z): ").lower().strip() # Convert to lowercase for uniformity
    if letter.isalpha() and len(letter) == 1:  # Check if it's a single alphabetical character
        if letter in 'aeiou':
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid input. Please enter a single letter (a-z or A-Z).")      

# Call the function
check_letter()


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

# Exercise 2: Old enough to vote?

def check_voting_eligibility():
    # Your control flow logic goes here
    try:
        # Capture the raw string input and strip spaces
        raw_input = input("Please enter your age: ").strip()
        
        # Guard clause: Ensure the input consists ONLY of digits (rejects '+', '-', and decimals)
        if not raw_input.isdigit():
            print("Invalid input. Please enter a valid positive integer for age.")
            return

        # Safe to convert to int now
        age = int(raw_input)
        
        voting_age = 18
        max_age = 120
        
        # Validate the age bounds
        if age > max_age:
            print(f"Invalid input. Please enter a realistic age between 0 and {max_age}.")
        elif age >= voting_age:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer for age.")

# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

# Exercise 3: Calculate Dog Years

def calculate_dog_years():
    # Your control flow logic goes here
    try:
        age = int(input("Input a dog's age: ").strip())
        
        # Guard clause: Ensure age is a realistic positive number
        if age <= 0:
            print("Invalid input. Age must be a positive integer greater than 0.")
            return
        
        # Calculate dog years based on the two-tiered rule
        if age <= 2:
            dog_years = age * 10
        else:
            # First 2 years = 20 dog years. Remaining years = 7 dog years each.
            dog_years = 20 + (age - 2) * 7
        
        print(f"The dog's age in dog years is {dog_years}.")
        
    except ValueError:
        print("Invalid input. Please enter a valid integer for the dog's age.")

# Call the function
calculate_dog_years()

