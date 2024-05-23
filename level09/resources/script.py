import sys

result = ""

for i, arg in enumerate(sys.argv[1]):
    result += chr(ord(arg)-i)

print(result)