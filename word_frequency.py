#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def word_frequency(text):
    """Calculate the frequency of each word in a given text."""
    # Convert text to lowercase to ensure case insensitivity
    text = text.lower()
    
    # Use regex to find words, ignoring punctuation (re.findall(pattern, string))
    # \b - word boundary
    # \w - any word character (letter, digit, underscore)
    # +  - one or more occurrences
    words = re.findall(r"\b[a-z]+(?:'[a-z]+)?", text)
    
    # Create a dictionary to hold word frequencies
    frequency = {}
    
    # Count the frequency of each word
    for word in words:
        # If word is already in dictionary, increase it's count
        if word in frequency:
            frequency[word] += 1
        # If word is not in dictionary, add it with count 1
        else:
            frequency[word] = 1
            
    return frequency

def print_word_frequencies(frequencies):
    """Print the word frequencies in a formatted way."""
    for word, count in frequencies.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    # Prompt the user for a sentence
    user_input = input("Please enter a sentence: ")
    # Validate the input and calculate word frequencies
    if is_sentence(user_input):
        # Calculate word frequencies and print them
        frequencies = word_frequency(user_input)
        print_word_frequencies(frequencies)
    # If the input is not a valid sentence, print an error message
    else:
        print("The provided text is not a valid sentence.")
