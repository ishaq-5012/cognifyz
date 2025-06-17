def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniform comparison
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Get input from user
input_str = input("Enter a word or phrase: ")

# Check and print result
if is_palindrome(input_str):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
