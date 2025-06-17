# --- List Examples ---
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)
numbers.append(6)
print("After append:", numbers)
numbers.pop()
print("After pop:", numbers)
print("First element:", numbers[0])

# Loop through list
for num in numbers:
    print("Square:", num ** 2)

# --- Tuple Examples ---
person = ("Alice", 25)
print("Name:", person[0])
print("Age:", person[1])

# Tuple unpacking
name, age = person
print("Unpacked:", name, age)

# --- defaultdict Example ---
from collections import defaultdict

text = "mississippi"
char_freq = defaultdict(int)
for char in text:
    char_freq[char] += 1
print("Character frequencies:", dict(char_freq))

# --- Control Structure Example ---
x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# --- Looping over collections ---
# Enumerate with list
for i, val in enumerate(numbers):
    print(f"Index {i}: Value {val}")

# Zip two lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# --- Function Examples ---

# Simple function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Function with default argument
def power(base, exponent=2):
    return base ** exponent

print("Power:", power(3))
print("Power with exponent:", power(3, 3))

# Function using *args and **kwargs
def print_args(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

print_args(1, 2, a=3, b=4)

# Lambda function
square = lambda x: x * x
print("Lambda square:", square(5))

# Filter prime numbers using function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = list(filter(is_prime, range(1, 21)))
print("Prime numbers:", primes)# Day 1 Exercises

# Your code here
