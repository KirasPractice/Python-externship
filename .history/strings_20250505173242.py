# # Create a string variable with the value "Python is amazing!".
# # Extract the following using slicing:
# # The first 6 characters ("Python") XXX
# # The word "amazing"
# # The entire string in reverse order
# # Print each of these slices with a clear label.
# # Example Output:

# # First word: Python
# # Amazing part: amazing
# # Reversed string: !gnizama si nohtyP


# pVar = "Python is amazing!"
# six_char = pVar[0:6]
# print(six_char)

# nine_char = pVar[10:17]
# print(nine_char)

# reversed_string = pVar[::-1]
# print(reversed_string)

# Task 2 - String Methods

# Create a string with the value " hello, python world! ".
# Use the following string methods and print the results:
# strip() to remove extra spaces
# capitalize() to capitalize the first letter
# replace() to replace "world" with "universe"
# upper() to convert the string to uppercase

backwords_string = "hello, python world!"
strip_back = backwords_string.strip()
print(strip_back)

cap_back = backwords_string[0:1].capitalize()

print(cap_back)



# Task 3 - Check for Palindromes
# Write a Python program to check if a string is a palindrome (reads the same backward and forward).
# Ask the user to input a word.
# Use slicing to reverse the string and compare it with the original.
# Print a friendly message indicating whether the word is a palindrome.
# Example Run:

# Enter a word: madam
# Yes, 'madam' is a palindrome!