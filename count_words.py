import string

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()

            # Remove punctuation and convert to lowercase
            text = text.translate(str.maketrans('', '', string.punctuation)).lower()

            words = text.split()
            word_count = {}

            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

            # Sort and display the result
            for word in sorted(word_count):
                print(f"{word}: {word_count[word]}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_name = input("Enter the name of the text file (e.g., sample.txt): ")
count_words_in_file(file_name)
