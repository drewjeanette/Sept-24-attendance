import random
import time

# ANSI escape codes for colors
RED = "\033[91m"
RESET = "\033[0m"

# Greet the user and get their name
varUserName = input("Hello! What's your name? ")

# Greet the user by name
print(f"Nice to meet you, {varUserName}! Let's generate some numbers for you.")

# Generate six random numbers
numbers = [random.randint(1, 69) for _ in range(5)]
numbers.append(random.randint(1, 26))

# Print the numbers with a delay and specific spacing
output = ""
for i, num in enumerate(numbers):
    time.sleep(0.25)  # Delay of 0.25 seconds
    if i < 5:
        output += f"{num}  "  # Two spaces between first 5 numbers
    else:
        # Print the last number in red
        output += f"    {RED}{num}{RESET}"  # Four spaces and red color for the last number
    
    # Use carriage return to print on the same line and update the output
    print(output, end="\r", flush=True)

# Print a final newline character to move to the next line
print()

# Farewell message
print("Hope you enjoyed your random numbers. Have a great day!")