import time
from random import uniform

def typing_effect(text, speed=None):
    """Prints text with a typing effect using a random delay for each character."""

    if speed == 'fast':
        print()
        for char in text:
            delay = uniform(0.01, 0.03)  # Random delay between 0.01 and 0.03 seconds
            print(char, end='', flush=True)  # Print without a newline, flush output buffer
            time.sleep(delay)  # Sleep for the random delay
        print()  # Make a space afterwards
    else:
        print()
        for char in text:
            delay = uniform(0.03, 0.1)  # Random delay between 0.03 and 0.1 seconds
            print(char, end='', flush=True)  # Print without a newline, flush output buffer
            time.sleep(delay)  # Sleep for the random delay
        print()  # Make a space afterwards
