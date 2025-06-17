import string

def check_password_strength(password):
    # Criteria
    min_length = 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    # Evaluate strength
    strength_score = sum([has_upper, has_lower, has_digit, has_special])

    # Check length
    if len(password) < min_length:
        return "Weak: Password is too short. Minimum 8 characters required."

    # Provide feedback based on score
    if strength_score == 4:
        return "Strong: Password meets all security criteria."
    elif strength_score == 3:
        return "Moderate: Add more character variety (e.g., special characters)."
    else:
        return "Weak: Password should include uppercase, lowercase, digits, and special characters."

# Example usage
user_password = input("Enter your password: ")
print(check_password_strength(user_password))
