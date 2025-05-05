# Task 1


# pVar = "Python is amazing!"
# six_char = pVar[0:6]
# print(six_char)

# nine_char = pVar[10:17]
# print(nine_char)

# reversed_string = pVar[::-1]
# print(reversed_string)

# Task 2 - String Methods


# backwords_string = "hello, python world!"
# strip_back = backwords_string.strip()
# print(strip_back)

# cap_back = backwords_string[0:1].capitalize()
# print(cap_back)

# replace_back = backwords_string[14:19].replace("world","universe")
# print(replace_back)

# upper_back = backwords_string.upper()
# print(upper_back)


# Task 3 - Check for Palindromes
# Write a Python program to check if a string is a palindrome (reads the same backward and forward).
# Ask the user to input a word. x
# Use slicing to reverse the string and compare it with the original.
# Print a friendly message indicating whether the word is a palindrome.
# Example Run:

# Enter a word: madam
# Yes, 'madam' is a palindrome!

user_word = input("Enter a word: ")
palindrome = user_word[::-1]

if user_word == palindrome:
    print("Wow! That word is a palondrome")
else:
    print("You, have a regular word")
