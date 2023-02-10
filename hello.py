# Ask user for their name
name = input("Whats your name? ")

# Say hello to user
print("Hello, "+name)
print("Hello,",name)
"""
Multi line comment
"""
print("Hello,",end ="")
print(name)

print("Hello, ",name)
print("Hello, ",name,sep="")
print("Hello, \"Friend\"")
print(f"Hello, {name}")

# Ask user for their name
name = input("What's your name? ")
# Remove whitespace from str
name = name.strip()

# Capitalize user's name (Cap first letter)
name = name.capitalize()

# Say hello to user
print(f"hello, {name}")

# Title based capitalization (cap first letter of each word)
name = name.title()
print(f"hello, {name}")

name = input("What's your name? ")
name = name.strip().title()

print(f"hello, {name}")

print(f"Hello,",input("What's your name? ").strip().title())

# Split user name into first name and last name
firstName, lastName = name.split(" ")
print(f"First Name: {firstName}\tLast Name: {lastName}")