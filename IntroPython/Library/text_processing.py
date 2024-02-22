# String
testString = "Dicoding"
print(testString.upper())
print(testString.lower())
print(testString.title())
print(testString.split('i'))
print(testString.zfill(20))

# Regex
import re

pattern = '^a...s$'
testString2 = 'abyss'
result = re.match(pattern, testString2)

if result:
    print('Search Successfully')
else:
    print('Search Failed')
