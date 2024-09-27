import time
from random import uniform

def typing_effect(text):
    """Prints text with a typing effect using a random delay for each character."""
    print()
    for char in text:
        delay = uniform(0.03, 0.1)  # Random delay between 0.03 and 0.08 seconds
        print(char, end='', flush=True)  # Print without a newline, flush output buffer
        time.sleep(delay)  # Sleep for the random delay
    print()  # Make a space afterwards