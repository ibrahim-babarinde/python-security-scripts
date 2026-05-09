#!/usr/bin/env python3
"""
===========================================
  Password Generator - by Ibrahim Babarinde
===========================================
  Generates strong, random passwords.
  Educational purposes only.
===========================================
"""

import random
import string


# ─────────────────────────────────────────
#  BUILD CHARACTER POOL
# ─────────────────────────────────────────

def get_characters(use_letters, use_numbers, use_symbols):
    """
    Builds the pool of characters the password
    will be generated from based on user choices.
    """
    characters = ""

    if use_letters:
        characters += string.ascii_letters  # a-z and A-Z
    if use_numbers:
        characters += string.digits         # 0-9
    if use_symbols:
        characters += string.punctuation    # !@#$%^&*() etc

    return characters


# ─────────────────────────────────────────
#  GENERATE PASSWORD
# ─────────────────────────────────────────

def generate_password(length, characters):
    """
    Randomly picks characters from the pool
    and builds a password of the chosen length.
    """
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


# ─────────────────────────────────────────
#  CHECK PASSWORD STRENGTH
# ─────────────────────────────────────────

def check_strength(length, use_letters, use_numbers, use_symbols):
    """
    Gives a simple strength rating based on
    length and character variety.
    """
    score = 0

    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    if use_letters:
        score += 1
    if use_numbers:
        score += 1
    if use_symbols:
        score += 1

    if score <= 2:
        return "Weak ❌"
    elif score <= 4:
        return "Moderate ⚠️"
    else:
        return "Strong ✅"


# ─────────────────────────────────────────
#  BANNER
# ─────────────────────────────────────────

def print_banner():
    print("=" * 50)
    print("       IBRAHIM'S PASSWORD GENERATOR")
    print("         Educational Purposes Only")
    print("=" * 50)


# ─────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────

def main():
    print_banner()

    # Get password length from user
    try:
        length = int(input("\nHow long should the password be? (e.g. 12): ").strip())
        if length < 4:
            print("[ERROR] Password must be at least 4 characters.")
            return
    except ValueError:
        print("[ERROR] Please enter a valid number.")
        return

    # Ask what character types to include
    print("\nWhat should the password include?")
    use_letters = input("Include letters? (y/n): ").strip().lower() == "y"
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == "y"

    # Build the character pool
    characters = get_characters(use_letters, use_numbers, use_symbols)

    # Make sure at least one type was selected
    if not characters:
        print("[ERROR] You must select at least one character type.")
        return

    # Ask how many passwords to generate
    try:
        count = int(input("\nHow many passwords to generate? (e.g. 5): ").strip())
        if count < 1:
            print("[ERROR] Must generate at least 1 password.")
            return
    except ValueError:
        print("[ERROR] Please enter a valid number.")
        return

    # Generate and display passwords
    print("\n" + "-" * 50)
    print(f"  Generated Passwords ({length} characters each)")
    print("-" * 50)

    for i in range(1, count + 1):
        password = generate_password(length, characters)
        print(f"  {i}. {password}")

    # Show strength rating
    strength = check_strength(length, use_letters, use_numbers, use_symbols)
    print("-" * 50)
    print(f"\n  Strength Rating: {strength}")
    print("\n  ⚠️  Never reuse passwords across accounts.")
    print("  ⚠️  Store them in a trusted password manager.")
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()