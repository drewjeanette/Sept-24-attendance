import random

# Greet the user and get their name
varUserName = input("Hello! What's your name? ")

# Greet the user by name
print(f"Nice to meet you, {varUserName}! Let's generate some numbers for you.")

# Generate six random numbers
num1 = random.randint(1, 69)
num2 = random.randint(1, 69)
num3 = random.randint(1, 69)
num4 = random.randint(1, 69)
num5 = random.randint(1, 69)
num6 = random.randint(1, 26)

# Print the numbers with specific spacing
print(f"{num1}  {num2}  {num3}  {num4}  {num5}    {num6}")

# Farewell message
print("Hope you enjoyed your random numbers. Have a great day!")