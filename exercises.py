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

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

# Exercise 4: Weather Advice

def weather_advice():
    # Your control flow logic goes here
    cold_input = input("Is it cold? (yes/no): ").strip().lower()
    raining_input = input("Is it raining? (yes/no): ").strip().lower()
    
    # Guard clause: Ensure the inputs are strictly 'yes' or 'no'
    valid_responses = ['yes', 'no']
    if cold_input not in valid_responses or raining_input not in valid_responses:
        print("Invalid input. Please answer with exactly 'yes' or 'no'.")
        return

    # Convert sanitized strings to clean boolean flags
    is_cold = cold_input == 'yes'
    is_raining = raining_input == 'yes'
    
    # Determine advice using logical operators
    if is_cold and is_raining:
        print("Wear a waterproof coat.")
    elif is_cold and not is_raining:
        print("Wear a warm coat.")
    elif not is_cold and is_raining:
        print("Carry an umbrella.")
    else:
        # Thanks to our guard clause, we know safely that this is NOT cold AND NOT raining
        print("Wear light clothing.")   

# Call the function
weather_advice()


# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

# Exercise 5: What's the Season?

def determine_season():
    # Your control flow logic goes here
    month_input = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()
    day_input = input("Enter the day of the month: ").strip()   
    
    # 1. Map months to their maximum allowed days
    month_days = {
        'Jan': 31, 'Feb': 29, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30,
        'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31
    }
    
    # Validate month input
    if month_input not in month_days:
        print("Invalid month input. Please enter a valid three-letter month (Jan - Dec).")
        return
        
    # Validate day input format
    if not day_input.isdigit():
        print("Invalid day input. Please enter a valid integer for the day.")
        return
        
    day = int(day_input)
    
    # 2. Validate the day against that specific month's calendar limit
    max_days = month_days[month_input]
    if day < 1 or day > max_days:
        print(f"Invalid day input. {month_input} only has days between 1 and {max_days}.")
        return

    # Determine season based on your perfectly structured condition trees
    if (month_input == 'Dec' and day >= 21) or (month_input in ['Jan', 'Feb']) or (month_input == 'Mar' and day <= 19):
        season = "Winter"
    elif (month_input == 'Mar' and day >= 20) or (month_input in ['Apr', 'May']) or (month_input == 'Jun' and day <= 20):     
        season = "Spring"
    elif (month_input == 'Jun' and day >= 21) or (month_input in ['Jul', 'Aug']) or (month_input == 'Sep' and day <= 21):
        season = "Summer"
    else:
        # Safely falls through to Fall due to strict prior validation
        season = "Fall"
        
    print(f"{month_input} {day} is in {season}.")

# Call the function
determine_season()

# Exercise 6: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

# Exercise 6: Number Guessing Game

def guess_number():
    # Your control flow logic goes here
    target_number = 42
    max_attempts = 5
    
    print(f"Welcome to the Number Guessing Game! Guess the number between 1 and 100.")
    
    for attempt in range(1, max_attempts + 1):
        if attempt == max_attempts:
            print("⚠️ Last chance!")
            
        while True:
            guess_input = input(f"Attempt {attempt}/{max_attempts} - Enter your guess: ").strip()
            
            if guess_input.isdigit():
                guess = int(guess_input)
                if 1 <= guess <= 100:
                    break
            
            print("Invalid input. Please enter a valid integer between 1 and 100.")

        if guess == target_number:
            print("Congratulations, you guessed correctly!")
            return 
        elif guess < target_number:
            print("Guess is too low.")
        else:
            print("Guess is too high.")
            
    # Reveal the number here if they exhaust all 5 attempts
    print(f"Sorry, you failed to guess the number in five attempts. The number was {target_number}!")

# Call the function
guess_number()