import random


# Generate a random number between 1 and 100
random_number = random.randint(1, 100)
print(f"Random number: {random_number}")
# Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")

# Generate random float between 0 and 1
random_float = random.random()
print(f"Random float: {random_float}")

# Simple calculator function
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

# Test calculator
result = calculator(10, 5, "+")
print(f"10 + 5 = {result}")

# Create a simple list and filter even numbers
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in my_list if num % 2 == 0]
print(f"Even numbers: {even_numbers}")
