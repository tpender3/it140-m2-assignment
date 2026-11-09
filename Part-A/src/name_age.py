"""This program asks for a name and age and calculates the birth year.

Input:
    Name: A string entered by the user.
    Age: An integer entered by the user.

Process:
    Subtract the user's age from the current year.

Output:
    A message showing the user's name and birth year on the screen.

Typical usage example:
    What is your name? Tukayicia
    How old are you? 30
    Hello Tukayicia! You were born in 1996.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("What is your name? ")
    age = int(input("How old are you? "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    print(f"Hello {name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===

