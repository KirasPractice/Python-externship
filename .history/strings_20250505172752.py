# Create a string variable with the value "Python is amazing!".
# Extract the following using slicing:
# The first 6 characters ("Python") XXX
# The word "amazing"
# The entire string in reverse order
# Print each of these slices with a clear label.
# Example Output:

# First word: Python
# Amazing part: amazing
# Reversed string: !gnizama si nohtyP


pVar = "Python is amazing!"
six_char = pVar[0:6]
print(six_char)

nine_char = pVar[10:17]
print(nine_char)

reversed_string = pVar[::-1]
print(reversed_string)
