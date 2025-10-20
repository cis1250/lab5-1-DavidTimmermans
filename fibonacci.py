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

def main():
    """Main program loop."""
    while True:
        # Ask user for input
        user_input = input("How many terms of the Fibonacci sequence do you want? ")
        # Check if input is valid
        n = validate_input(user_input)
        # If valid, generate and print the Fibonacci sequence
        if n is not None:
            sequence = fibonacci(n)
            print(f"Fibonacci sequence ({n} terms):", *sequence)
            break

if __name__ == "__main__":
    main()

