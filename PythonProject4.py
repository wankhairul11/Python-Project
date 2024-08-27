def check_positive_number(num):
    if num < 0:
        raise ValueError("The number must be positive!")
    return num

# Example usage:
try:
    # Get user input
    user_input = int(input("Enter a number: "))
    
    # Check if the number is positive
    result = check_positive_number(user_input)
    
    # If the number is positive, print it
    print(f"The number {result} is positive.")
    
except ValueError as e:
    # Handle the case where the number is not positive
    print(f"Error: {e}")
