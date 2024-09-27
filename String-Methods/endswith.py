# endswith()
# it gives you True if the string ended with given suffix otherwise it gives the false

# Original string
virat = 'Virat Kohli is the best player in the world'

# Check if the string ends with a specific suffix
suffix_1 = 'world'
suffix_2 = 'player'

# Use endswith() method
result_1 = virat.endswith(suffix_1)
result_2 = virat.endswith(suffix_2)

# Print the results
print(f"Does the string end with '{suffix_1}'? {result_1}")
print(f"Does the string end with '{suffix_2}'? {result_2}")
