# Open a file
plain_file = open('plain_text.txt', mode='r')
# Print file content on screen
print(plain_file.read())
# Check whether file is closed
print(plain_file.closed)
# Close the file
plain_file.close()
# Check whether file is closed
print(plain_file.closed)