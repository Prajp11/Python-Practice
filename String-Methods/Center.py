# Center()
# It gets the string in the middle
# The center() method returns a new string of a specified length with the original string centered in it. 
# If the total width is greater than the original string length, it adds padding characters (spaces by default) on both sides. 
# Optionally, you can specify a different character for padding.

string = 'Prajwal'
centered_string_1 = string.center(10)

# Center the string with total width of 18 and pad with '*'
centered_string_2 = string.center(18, '*')
print("Centered with width 10 (space padding):", centered_string_1)
print("Centered with width 18 (*** padding):", centered_string_2)

