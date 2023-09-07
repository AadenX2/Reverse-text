# https://github.com/sepandhaghighi/art
from art import *

# "reverseString" is a function that takes a string as an argument and returns the reverse of that string. 
# now that "reverseString" is a function, we can call it anywhere in our code and it will run the code inside the function.
def reverseString(s):
    return s[slice(None, None, -1)]


# test
reversed = reverseString("super")
pretty = text2art(reversed)
print(pretty) 