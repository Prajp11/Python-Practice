# find() 
# It gives you the index number of your substring in the your main string.

# The find() method in Python is used to return the lowest index of the substring if it is found in the main string. 
# If the substring is not found, it returns -1.


main_string = 'Virat Kohli is the best player in the world'
# substring = 'best'
# index = main_string.find(substring)
# print(f"The substring '{substring}' is found at index {index}.")



# Substring that doesn't exist in the string
substring_not_found = 'Sachin'

# Use find() to get the index of the substring
index_not_found = main_string.find(substring_not_found)

# Print the result
print(f"The substring '{substring_not_found}' is found at index {index_not_found}.")

