# Given a list of numbers, remove all occurrences of a specific number and calculate the sum of remaining numbers.

numbers = [1, 2, 3, 4, 5, 3, 6, 7, 3]  # List of numbers
remove_num = 3  # The number to be removed

# Remove all occurrences of remove_num
while remove_num in numbers:
    numbers.remove(remove_num)

# Print the result
print("Numbers after removal:", numbers)
print("Sum of remaining numbers:", sum(numbers))
