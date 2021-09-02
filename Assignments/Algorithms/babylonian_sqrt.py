# Breaking down the babylonian square root algorithm 
# Chapter 3.5 
# The Practice of Computing Using Python

"""
(a) Guess the square root of the number.
(b) Divide the number by the guess.
(c) Average the quotient (from step b) and the guess.
(d) Make the new guess the average from step (c).
(e) If the new guess differs from the previous guess by more than the specified
tolerance, go back to step (b); otherwise, stop
"""
try:
    # Don't change these lines
    number = int(input("Find the square root of integer: "))
    guess = int(input("Initial guess: "))
except ValueError:
    print("[!] Please enter an integer")
    exit(0)

try:
    tolerance = float(input("What tolerance: "))
except ValueError:
    print("[!] Please enter a float value")
    exit(0)

# Implement the Babylonian square root algorithm

try:
    count = 0
    previous_guess = 0
    
    while abs(previous_guess - guess) > tolerance:
        previous_guess = guess
        quotient = number / guess
        guess = (quotient + guess) / 2
        count += 1
except Exception as e:
    print(e)

# Don't change these lines
print("Square root of", number, "is", round(guess, 4))
print("Took", count, "reps to get it to tolerance")