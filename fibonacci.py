#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

def validate_input(user_input):
    """Validate that the input is a positive integer."""
    try:
        # Convert input to integer
        value = int(user_input)
        # Check if the value is positive
        if value > 0:
            return value
        # If not positive, return None
        print("Invalid input. Please enter a positive integer.")
        return None
    # If non-integer input, return None
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return None

def fibonacci(term):
    """Generate Fibonacci sequence up to n terms."""
    # Check if input is an integer and positive
    if not isinstance(term, int) or term <= 0:
        return None

    # Initialize the Fibonacci sequence
    if term == 1:
        return [0]
    if term == 2:
        return [0, 1]
        
    # Generate the Fibonacci sequence
    fib_sequence = [0, 1]
    for _ in range(2, term):
        # Calculate the next Fibonacci number and append it to the list
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


def print_fibonacci(sequence):
    """Print the Fibonacci sequence."""
    for num in sequence:
        print(num, end=' ')

if __name__ == "__main__":
    # Loop until valid input is received
    while True:
        # Prompt the user for the number of terms
        user_input = input("Enter the number of terms for the Fibonacci sequence: ")
        n = validate_input(user_input)
        
        # If input is valid, generate and print the Fibonacci sequence and break the loop
        if n is not None:
            sequence = fibonacci(n)
            print_fibonacci(sequence)
            break
