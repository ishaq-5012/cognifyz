def generate_fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci sequence: 0")
    elif n == 2:
        print("Fibonacci sequence: 0, 1")
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            next_term = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_term)
        print("Fibonacci sequence:", ', '.join(map(str, fib_sequence)))

# Example usage
try:
    num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
    generate_fibonacci(num_terms)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
