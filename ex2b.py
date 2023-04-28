item_number = 27.283
print(f"My item num is {item_number}.")
print(f"My item num is {item_number:10}. Notice that it is padded with spaces.") 
print(f"My item num is {item_number:.2f}, rounded to two decimal places.")

## Note:
## The "f" that preceeds the string, that is, f"hello", means "format".
## The "f" inside the curly braces, that is, {item_number:.2f}, means "floating point number".

print(f"This one is both rounded and has extra space: {item_number:9.2f}. Do you see?")
print(f"If the extra space is small, it may not change how the number is printed, such as in this case: {item_number:3.2f}.")

####################

print("You can also center the value within the available space.")
print("I'll add some letters before and after to make it clear:")
print(f"words{item_number:^11.2f}words")


print(f"Here's how to left-align: {item_number:<11.2f}")

another_num = 17
print("Here's how to display in binary, octal, hexadecimal:")
print(f"The number {another_num}, expressed in binary, is {another_num:b}.")
print(f"The number {another_num}, expressed in octal, is {another_num:o}.")
print(f"The number {another_num}, expressed in hexadecimal, is {another_num:x}.")

## Incidentally, the format code "d" means decimal, which is the default:
print(f"The number {another_num}, expressed in decimal, is {another_num:d}.")

## You can also display the number with a prefix that indicates the number system:
print(f"The number {another_num}, expressed in binary, is {another_num:#b}.")
print(f"The number {another_num}, expressed in octal, is {another_num:#o}.")
print(f"The number {another_num}, expressed in hexadecimal, is {another_num:#x}.")

## Note that the format specifiers for other number systems don't work for floats:
# item_number = 27.283
# print(f"This will give an error, because item_number is a float: {item_number:b}.")


## For more information:
## -  This website gives some great practical examples. Recommended to start here.
##    https://www.linisnil.com/articles/practical-guide-to-python-string-format-specifiers/
## -  Another good site:
##    https://www.pythonmorsels.com/string-formatting/
## -  This website gives detailed documentation; somewhat more difficult to read.
##    https://docs.python.org/3/library/string.html#format-specification-mini-language