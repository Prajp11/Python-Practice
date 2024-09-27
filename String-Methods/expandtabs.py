# expandtabs()
# It expanding the space in our given string
# The expandtabs() method in Python is used to replace tab characters (\t) in a string with spaces. 
# The number of spaces is based on the tab size specified, which defaults to 8 spaces if not provided.

# Original string with tab characters
string_with_tabs = 'Virat\tKohli\tis\tthe\tbest'

# Expanding tabs to the default size (8 spaces)
expanded_default = string_with_tabs.expandtabs()

# Expanding tabs to a custom size (e.g., 4 spaces)
expanded_custom = string_with_tabs.expandtabs(4)

# Print the results
print("Original string:", string_with_tabs)
print("Expanded with default tab size (8 spaces):", expanded_default)
print("Expanded with custom tab size (4 spaces):", expanded_custom)
