def is_valid_email(email):
    if "@" not in email or email.count("@") != 1:
        return False

    username, domain = email.split("@")

    if not username or not domain:
        return False

    if "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    return True

# Taking input from the user
email_input = input("Enter an email address: ")

# Validating the email
if is_valid_email(email_input):
    print("Valid email address.")
else:
    print("Invalid email address.")
