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

# Finding a phone number in a longer string (i.e. a string generated from interpretating voice input)
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumber(chunk):
            print('Phone number found: ' + chunk)
    print('Done')
# This takes a 12 character long chunk of the message every loop iteration, getting nudged down the message by one every time. Very inefficient way to do it.

# Above is a lot of code for a small task, and is also very limited. It cannot detect extensions or numbers formatted differently (. instead of -, etc.)
# It can't detect other types of phone numbers either, i.e. UK ones

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# Checking for a phone number via Regular Expression (aka Regex)
# Handy-dandy Regex guide: https://www.regular-expressions.info/

# Regex is a description for a pattern of text.
# \d = digit character, a single numeral from 0 to 9
# This regex covers the large chunk of code above: \d\d\d-\d\d\d-\d\d\d\d
    # 3 digits, a hyphen, another 3 digits and a hyphen, then the final 4 digits
    # This would also cover it: \d{3}-\d{3}-\d{4}
    # using {NUMBER} will do the action multiple times, so \d{3} is shorthand for \d\d\d

# In Python, regex is stored in the "re" module
import re

# Passing a string representing a regular expression to re.compile() returns a Regex pattern object (or simply, a Regex object).
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # the "r" is to make the string into a raw string, 
                                                      # which means the backslashes are interpreted as just backslashes, 
                                                      # not as a part of a special character (i.e \n for newline)

mo = phoneNumRegex.search('My number is 415-555-4242.')
# mo means "Match Object", just a generic variable name
# Regex objects have a search() method that checks the string (string only!) that then returns a Match object if something is found, or None if it doesn't.

# Match objects have a group() method that will return the actual matched text from the searched string.
print(mo.group()) # This would print "415-555-4242"

# Alternatively, if we don't want to create a Regex object, we can skip straight to the Match object by using search() like this:
    # re.search(pattern, string, flags=0) 
        # flags are optional
mo = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', 'My number is 415-555-4242.')
# This returns a Match object without requiring the creation of a Regex object first
    # Useful if you only need to regex one thing once

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# Regex grouping
# Adding parentheses to a regex will split it into groups, i.e.:
# (\d\d\d)-(\d\d\d-\d\d\d\d)
# This would search for the whole string, similar to above, but splits the matched string out into two

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
# returns '415'
mo.group(2)
# returns '555-4242'
mo.group(0)
# returns '415-555-4242'
mo.group()
# returns '415-555-4242'

# To get all groups back at once, do this:
mo.groups()
# returns a tuple of strings ('415', '555-4242')
# You can also store the tuple items in separate variables, like so:
areaCode, mainNumber = mo.groups()

# If you need to match a parentheses as part of a regex, they need escaping with a backslash as () are special characters in regex. Example:
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.group(1)
# returns '(415)'
mo.group(2)
# returns '555-4242'

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# Matching multiple groups with a pipe character
# | is a pipe, can be used anywhere you want to match one of many expressions.
# If a pipe is part of the regex you want to match, it must be escaped via a backslash (\|)
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.') # This will only return the first match, in this case 'batman'
mo1.group()
# returns 'Batman'

mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group()
# returns 'Tina Fey'

# findall() method can be used to find all matches in a string

# Pipe can also be used to match one of several patterns in regex
    # i.e. If you want to match Batman related things (Batman, Batmobile, Batcopter, Batarang, etc.)
    # you can use the following:
batRegex = re.compile(r'Bat(man|mobile|copter|bat)') # This is done by having the strings you want to match in parentheses with a "prefix" to the left of the opening bracket
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
# returns 'Batmobile'
# group() will always return the full matched text - the prefix and text.

mo.group(1)
# returns 'mobile'
# group(number) will return just part of the matched text, without the prefix.

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# Optional matching with a question mark character
    # Patterns can be matched optionally by use of a ?

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
'Batwoman'

# (wo) ? part of the expression means the pattern "wo" is optional. Hence, this expression will match both "Batman" and "Batwoman"
# Question marks will only match text where there is zero or one instance of the optional text in it.
    # Doesn't appear that it would match if the text was "Batwomanwo"
    # Multiple match is for star/asterisk

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# Matching zero or more with a star/asterisk

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
'Batwoman'

mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()
'Batwowowowoman'

# (wo) * part of the regex can match multiple times
    # "Batman" 0 matches
    # "Batwoman" 1 match
    # "Batwowowowoman" 4 matches
# For an actual star character in a string, use \*

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# Matching one or more with a +

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()
'Batwoman'

mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()
'Batwowowowoman'

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None
True

# + symbol matches one or more - requires at least one match to return something.
# \+ to have an actual plus symbol in a string

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# Matching a specific number of repetitions
    # Using a set of curly brackets {}, a regex can be set to look for a specific string X number of times in a row.
    # i.e. (Ha){3} will match a string of "HaHaHa", but not "HaHa"

# A range can also be used, which will look for matches for the string anywhere between the minimum and maximum values
    # i.e. (Ha){3,5} - (HaHaHa) to (HaHaHaHaHa)
    # can match 3, 4 or 5 instance of the search string

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# Greedy and non-greedy matching
    # Python's regexes are greedy by default, meaning in an ambiguous situation they will match the longest string possible.
    # Non-greedy matching will match the shortest string possible.

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()
'HaHaHaHaHa'

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()
'HaHaHa'

# The question mark after the {} is to set the matching to non-greedy
    # Note that the question mark can have two meanings in a regex - either declaring a non-greedy match, or flagging an optional group.