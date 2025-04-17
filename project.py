import re

def check_password_strength(password):
    try:
        if not isinstance(password, str):
            raise TypeError("Password must be a string.")

        # Initialize score
        score = 0

        # Check length
        if len(password) >= 8:
            score += 1
        else:
            print("❌ Password should be at least 8 characters long.")

        # Check for lowercase letters
        if re.search(r"[a-z]", password):
            score += 1
        else:
            print("❌ Add some lowercase letters.")

        # Check for uppercase letters
        if re.search(r"[A-Z]", password):
            score += 1
        else:
            print("❌ Add some uppercase letters.")

        # Check for digits
        if re.search(r"\d", password):
            score += 1
        else:
            print("❌ Add at least one digit.")

        # Check for special characters
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1
        else:
            print("❌ Add a special character like !, @, #, etc.")

        # Return score
        return score

    except TypeError as te:
        print(f"TypeError: {te}")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0

# Loop until strong password is entered
while True:
    try:
        password = input("Enter a password to check: ")
        strength = check_password_strength(password)

        if strength == 5:
            print("✅ Strong password accepted!")
            break
        else:
            print("Please try again with a stronger password.\n")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        break
