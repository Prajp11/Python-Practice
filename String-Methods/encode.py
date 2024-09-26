# encode()
# It is used to convert the string into a bytes object, using encoding format (default is 'utf-8').
# The b at the start indicates it's a bytes object, and the string has been encoded using the UTF-8 encoding.

# Original string
virat = 'Virat Kohli is the best player in the world and Virat Kohli is the best batsman in the planet'

# Convert the string to bytes using the default utf-8 encoding
encoded_virat = virat.encode()

# Print the encoded bytes object
print(encoded_virat)

