print("===== STRING METHODS DEMO =====\n")

s = "  Hello Shubham Kore"
num = "12345"
alpha = "shubham kore"
alnum = "shubhamkore123"
space = "   "

# Case Conversion Methods
print("CASE METHODS")
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print("shubham kore".swapcase())
print("-" * 40)

# Checking / Validation Methods
print("CHECKING METHODS")
print(alpha.isalpha())
print(num.isdigit())
print(alnum.isalnum())
print(space.isspace())
print("shubham kore".islower())
print("shubham kore".isupper())
print("-" * 40)

# Searching & Finding Methods
print("SEARCHING METHODS")
text = "hello world hello"
print(text.find("world"))
print(text.rfind("hello"))
print(text.index("hello"))
print(text.count("hello"))
print("-" * 40)

# String Modification Methods
print("MODIFICATION METHODS")
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(text.replace("shubham kore","hello"))
print("_"*40)


# Splitting & Joining
print("SPLIT AND JOIN")
fruits="apple,banana,mango"
print(fruits.split(","))
print(fruits.rsplit(",",1))
words = ["Python", "is", "awesome"]
print(" ".join(words))
print("-" * 40)

# Formatting Methods
print("FORMATTING")
name = "Shubham"
age = 22
print("My name is {} and age is {}".format(name, age))
print(f"My name is {name} and age is {age}")
print("-" * 40)

# Alignment & Padding
print("ALIGNMENT METHODS")
word = "Shubham"
print(word.center(10, "*"))
print(word.ljust(10, "-"))
print(word.rjust(10, "-"))
print("-" * 40)

# Prefix & Suffix Checking
print("PREFIX & SUFFIX")
file = "program.py"
print(file.startswith("program"))
print(file.endswith(".py"))
print("-" * 40)

# Encoding & Decoding
print("ENCODE & DECODE")
encoded = alpha.encode()
print(encoded)
decoded = encoded.decode()
print(decoded)
print("-" * 40)

# Other Useful Methods
print("OTHER METHODS")
print("hello".zfill(10))
print("HELLO".casefold())
print("one\ntwo\nthree".splitlines())
print("Hello\tPython".expandtabs(5))