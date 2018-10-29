# From https://automatetheboringstuff.com/chapter7/
# ---- Regular Expressions ---- #

# Checking a (American) phone number without REs
def isPhoneNumber(text):
    if len(text) != 12:   # Phone number is only 12 characters, so if it's longer or shorter than 12 it can't be a phone number
        return False
    for i in range(0, 3):   # Are all of the first 3 characters a number?
        if not text[i].isdecimal():
            return False
    if text[3] != '-':   # 4th character MUST be a hyphen
        return False
    for i in range(4, 7):   # Are the middle 3 characters numbers?
        if not text[i].isdecimal():
            return False
    if text[7] != '-': # 8th character MUST be a hyphen
        return False
    for i in range(8, 12):   # Last 4 characters must be numbers too
        if not text[i].isdecimal():
            return False
    return True

# Quite long-winded, lots of steps which makes it easy to make mistakes.