# Small Exercise 1. Hello You

# Prompt the user for his name using the input function.
name = input("What is your name? ")

# Upon receiving their name, you will say hello to them.
print("Hello " + name)


# Small Exercise 2. HELLO YOU

# Repeat the above exercise but this time print the user's name in ALL CAPS, and also tell them the number of letters in their name.
name = input("What is your name? ")
print("Hello " + name.upper()+ ". Your name has %d letters in it! Awesome!" % (len(name)))
