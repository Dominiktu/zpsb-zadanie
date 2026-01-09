import random


# Generate a random number between 1 and 100
random_number = random.randint(1, 100)
print(f"Random number: {random_number}")
# Generate a random choice from a list
choices = ["apple", "banana", "orange", "grape"]
random_choice = random.choice(choices)
print(f"Random choice: {random_choice}")
# Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")
