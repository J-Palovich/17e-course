# convert number to binary (has "0b" prefix )
print(bin(17))
print(f"An arbitrary number in binary: {bin(17)}")

# convert to binary without prefix
# print(bin(17:b)) DOES NOT WORK
print(f"An arbitrary number in binary without a prefix: {17:b}")

# Hexadecimal and octal examples
# with prefixes
print(f"An arbitrary number in octal: {oct(17)}")
print(f"An arbitrary number in hexadecimal: {hex(17)}")
# without prefixes
print(f"An arbitrary number in octal without a prefix: {17:o}")
print(f"An arbitrary number in hexadecimal without a prefix: {17:x}")

# Note that functions work alone, but the format specifiers don't:
## This works:
exampleVar = bin(6)
print(f"The value is {exampleVar}.")

## This won't work:
# exampleVar = {6:b}
# print(f"The value is {exampleVar}.")