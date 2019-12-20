# Import the regular expression module
import re
print("****** Example 1: match Phone Number *****")
# Compile the pattern: pattern
pattern = re.compile('\d{3}-\d{3}-\d{4}')
# See if the pattern matches
result = pattern.match('123-456-7890')
print(bool(result))
# See if the pattern matches
result = pattern.match('1123-456-7890')
print(bool(result))
print("****** Example 2: verify dollar amount format *****")
pattern = re.compile('\$\d*.\d{2}')
result = pattern.match('$13.25')
print(bool(result))



