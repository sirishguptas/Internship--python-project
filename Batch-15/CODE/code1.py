
# Save user credentials to a file
with open(credentials_file, "w") as credentials_file:
    json.dump(users, credentials_file, indent=2)
import os
import json
import inspect
import math
from fuzzywuzzy import process
from getpass import getpass
import shutil

# Function to check login credentials
def login(users):
    user_id = input("Enter User ID: ")
    password = getpass("Enter Password: ")

    if user_id in users and users[user_id]["password"] == password:
        print(f"Login successful for {user_id}!\n")
        return user_id
    else:
        print("Incorrect User ID or Password. Exiting...\n")
        return None

# Function to register a new user
def register_user(users):
    new_user_id = input("Enter a new User ID (Enter 'E' to finish registration): ")

    if new_user_id.upper() == 'E':
        return None

    if new_user_id in users:
        print("User ID already exists. Try a different one.")
        return register_user(users)
    else:
        new_password = getpass("Create a Password: ")
        users[new_user_id] = {"password": new_password, "docs": {}, "operations_file": f"{new_user_id}_operations.txt"}
        user_folder = os.path.join(users_folder, new_user_id)
        os.makedirs(user_folder, exist_ok=True)
        print(f"User {new_user_id} registered successfully!\n")
        return new_user_id

# Function to save documentation for a user
def save_documentation(user_id, function_name, function_signature, function_docstring):
    user_docs_folder = os.path.join(users_folder, user_id)
    doc_path = os.path.join(user_docs_folder, f"{function_name}_doc.txt")

    with open(doc_path, "w") as doc_file:
        doc_file.write(f"Function: {function_name}\n")
        doc_file.write(f"Signature: {function_signature}\n\n")
        doc_file.write(f"Docstring:\n{function_docstring}\n\n")

# Function to save user operations to their operations file
def save_user_operations(user_id, operation_description):
    user_operations_file = os.path.join(users_folder, users[user_id]["operations_file"])
    
    with open(user_operations_file, "a") as operations_file:
        operations_file.write(f"{operation_description}\n")

# Function to copy all documentation files to the documentation folder
def copy_documentation_to_project(users, documentation_folder):
    for user_id, user_data in users.items():
        user_docs_folder = os.path.join(users_folder, user_id)

        for doc_file_name in os.listdir(user_docs_folder):
            if doc_file_name.endswith("_doc.txt"):
                doc_path = os.path.join(user_docs_folder, doc_file_name)
                shutil.copy(doc_path, os.path.join(project_folder, documentation_folder))

# ... (Rest of the functions remain unchanged)
def add(a,b):  
    """
    Perform addition operation on two numbers.

    :param a: The first number.
    :param b: The second number.
    :return: Result of the addition operation.
    
    Pseudocode:
    
    return a + b """

def subtract(a, b):
    """
    Perform subtraction operation on two numbers.

    :param a: The first number.
    :param b: The second number.
    :return: Result of the subtraction operation.
   
   
    Pseudocode:
    
    return a - b"""

def multiply(a, b):
    """
    Perform multiplication operation on two numbers.

    :param a: The first number.
    :param b: The second number.
    :return: Result of the multiplication operation.
    
    Pseudocode:
    
    return a * b"""

def divide(a, b):
    """
    Perform division operation on two numbers.

    :param a: The numerator.
    :param b: The denominator.
    :return: Result of the division operation.
    
    Pseudocode:
    
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero." """

def swap(a, b):
    """
    Swap the values of two variables.

    :param a: The first variable.
    :param b: The second variable.
    
    Pseudocode:
    
    temp = a
    a = b
    b = temp """

def sum_digits(number):
    """
    Calculate the sum of digits of a number.

    :param number: The input number.
    :return: The sum of digits.
    
    Pseudocode:
    
    number_string = str(number)
    return sum(int(digit) for digit in number_string)"""

def is_prime(number):
    """
    Check if a number is prime.

    :param number: The input number.
    :return: True if the number is prime, False otherwise.
    
    Pseudocode:
    
    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True """

def is_palindrome(string):
    """
    Check if a string is a palindrome.

    :param string: The input string.
    :return: True if the string is a palindrome, False otherwise.
    
    Pseudocode:
    
    string = string.lower()
    return string == string[::-1] """

def count_vowels(string):
    """
    Count the number of vowels in a string.

    :param string: The input string.
    :return: The number of vowels in the string.
    
    Pseudocode:
    
    return sum(1 for char in string.lower() if char in "aeiou")"""

def reverse_string(string):
    """
    Reverse a given string.

    :param string: The input string.
    :return: The reversed string.
    
    Pseudocode:
    
    return string[::-1] """

def find_extremes(lst):
    """
    Find the maximum and minimum elements in a list.

    :param lst: The input list.
    :return: A tuple containing the maximum and minimum elements.
    
    Pseudocode:
    
    if not lst:
        return None

    max_val = min_val = lst[0]

    for element in lst:
        if element > max_val:
            max_val = element
        elif element < min_val:
            min_val = element

    return max_val, min_val """

def calculate_square_root(number):
    """
    Calculate the square root of a number.

    :param number: The input number.
    :return: The square root of the number.
    
    Pseudocode:
    
    return math.sqrt(number)"""

def fibonacci(n):
    """
    Calculate the nth Fibonacci number.

    :param n: The position of the Fibonacci number to calculate.
    :return: The nth Fibonacci number.
    
    Pseudocode:
    
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)"""

def factorial(n):
    """
    Calculate the factorial of a number.

    :param n: The number to calculate the factorial.
    :return: The factorial of the given number.
    
    Pseudocode:
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)"""

def percentage(a, b):
    """
    Calculate the percentage of a number.

    :param a: The part.
    :param b: The whole.
    :return: The percentage.
    
    Pseudocode:
    
    return (a / b) * 100"""

def binary_to_decimal(binary_string):
    """
    Convert a binary string to a decimal number.

    :param binary_string: The binary string.
    :return: The decimal equivalent of the binary string.
    
    Pseudocode:
    
    return int(binary_string, 2)"""

def is_armstrong_number(number):
    """
    Check if a number is an Armstrong number.

    :param number: The input number.
    :return: True if the number is an Armstrong number, False otherwise.
    
    Pseudocode:
    
    num_str = str(number)
    order = len(num_str)
    sum_powered_digits = sum(int(digit) ** order for digit in num_str)
    return sum_powered_digits == number """

def find_common_elements(list1, list2):
    """
    Find the common elements between two lists.

    :param list1: The first input list.
    :param list2: The second input list.
    :return: A list containing the common elements.
    
    Pseudocode:
    
    return list(set(list1) & set(list2))"""
# Dictionary to map function names to their corresponding functions
functions = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "swap": swap,
    "sum_digits": sum_digits,
    "is_prime": is_prime,
    "is_palindrome": is_palindrome,
    "count_vowels": count_vowels,
    "reverse_string": reverse_string,
    "find_extremes": find_extremes,
    "calculate_square_root": calculate_square_root,
    "fibonacci": fibonacci,
    "factorial": factorial,
    "percentage": percentage,
    "binary_to_decimal": binary_to_decimal,
    "is_armstrong_number": is_armstrong_number,
    "find_common_elements": find_common_elements,
}

# Main program
project_folder = "my_project"
documentation_folder = "documentation_operations"
users_folder = "users"
credentials_file = "users_credentials.json"

# Create project folder if it doesn't exist
os.makedirs(project_folder, exist_ok=True)

# Create a folder for documentation operations
os.makedirs(os.path.join(project_folder, documentation_folder), exist_ok=True)

# Create a folder for users
os.makedirs(users_folder, exist_ok=True)

# Load or create user credentials file
if os.path.exists(credentials_file):
    with open(credentials_file, "r") as credentials_file:
        users = json.load(credentials_file)
else:
    users = {}

# Check login credentials or register a new user
logged_in_user = None
while not logged_in_user:
    user_option = input("Do you want to (L)ogin, (R)egister a new user, or (X) Exit? ").upper()
    if user_option == 'L':
        logged_in_user = login(users)
    elif user_option == 'R':
        logged_in_user = register_user(users)
        if logged_in_user:
            # If registration is successful, ask for login again
            logged_in_user = login(users)
    elif user_option == 'X':
        print("Exiting the program. Goodbye!")
        exit()
    else:
        print("Invalid option. Please choose 'L' or 'R' or 'X' to exit.")

# User interface to generate documentation files
while True:
    function_name_input = input("Enter the function name (E to exit, LO to Log Out): ")

    if function_name_input.upper() == 'E':
        break
    elif function_name_input.upper() == 'LO':
        print(f"Logging out {logged_in_user}...\n")
        # Copy all documentation files to the documentation folder
        copy_documentation_to_project(users, documentation_folder)
        logged_in_user = None
        while not logged_in_user:
            user_option = input("Do you want to (L)ogin, (R)egister a new user, or (X) Exit? ").upper()
            if user_option == 'L':
                logged_in_user = login(users)
            elif user_option == 'R':
                logged_in_user = register_user(users)
                if logged_in_user:
                    # If registration is successful, ask for login again
                    logged_in_user = login(users)
            elif user_option == 'X':
                print("Exiting the program. Goodbye!")
                exit()
            else:
                print("Invalid option. Please choose 'L' or 'R' or 'X' to exit.")
    else:
        # Check if the input matches any function name or its abbreviation
        function_name = None
        for func_name, func in functions.items():
            if function_name_input.lower() in [func_name.lower(), func_name[:3].lower()]:
                function_name = func_name
                break

        if function_name:
            selected_function = functions[function_name]

            # Generate documentation dynamically for the selected function
            function_signature = inspect.signature(selected_function)
            function_docstring = inspect.getdoc(selected_function)

            # Write documentation to a file
            save_documentation(logged_in_user, function_name, function_signature, function_docstring)

            # Save user operations to their operations file
            operation_description = f"{logged_in_user} performed {function_name} operation."
            save_user_operations(logged_in_user, operation_description)

            # Display the saved documentation
            user_docs_folder = os.path.join(users_folder, logged_in_user)
            doc_path = os.path.join(user_docs_folder, f"{function_name}_doc.txt")
            try:
                with open(doc_path, "r") as doc_file:
                    print(f"\nContents of {function_name}_doc.txt:\n")
                    print(doc_file.read())
            except FileNotFoundError:
                print(f"{function_name}_doc.txt not found.")
        else:
            # Get close matches using fuzzywuzzy
            close_matches = process.extract(function_name_input, functions.keys(), limit=3)

            # Display close match suggestions
            print(f"Function not found. Did you mean one of these? {close_matches}")

# Save user credentials to a file
with open(credentials_file, "w") as credentials_file:
    json.dump(users, credentials_file, indent=2)
