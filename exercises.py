"""
STRINGS — PRIMM Exercises
=========================

Work through each activity in order. For each one, follow the PRIMM steps
written in the comments:

    PREDICT     — read the code and write down what you think it will do
    RUN         — run it and compare
    INVESTIGATE — try different inputs and dig into why it behaves that way
    MODIFY      — fix or extend the code as instructed
    MAKE        — write your own function from scratch

Work in pairs. It's not a race — understanding the first two activities
fully is more valuable than rushing to the end.
"""


# ==============================================================================
# ACTIVITY 1: Iterating over strings
# ==============================================================================
#
# A string is a sequence of characters. You can step through it one character
# at a time using a for loop, just like you would with a list.
#
# PREDICT: What will print_each_character("hello") print?
#          How many lines will appear? 5
#          h
#          e
#          l
#          l
#          o
#
# RUN: Call the function at the bottom of the file and check.
#
# INVESTIGATE: Try it with:
#   - a single character, e.g. "a"
#   - an empty string ""
#   - a string with spaces, e.g. "hi there"
# ==============================================================================

def print_each_character(text):
    for char in text:
        print(char)


# MODIFY -----------------------------------------------------------------------
# The function below should print the index AND the character on each line,
# like this:
#
#   0: h
#   1: e
#   2: l
#   3: l
#   4: o
#
# Right now it only prints the character. Fix the print() line so it
# also shows the position.
# ------------------------------------------------------------------------------

def print_with_positions(text):
    # text = text[:1]
    for i in range(len(text)):
        print(f"{i}: {text[i]}")          # ← fix this line
        #print(f"{i+1}: {text[i]}")          # ← fix this line


# MAKE -------------------------------------------------------------------------
# Complete this function so it counts the number of characters in a string
# WITHOUT using len(). Use a loop instead — add 1 to a counter for each
# character you find.
# ------------------------------------------------------------------------------

def string_length_manual(text):
    # TODO: count characters using a loop
    count = 0
    for char in text:
        count = count +1
    return count
    


# ==============================================================================
# ACTIVITY 2: Searching strings — looking at characters one by one
# ==============================================================================
#
# PREDICT: How many 'a's are in "banana"?
#          What about in "Apple" — will it count the capital A?
#
# RUN: Try count_letter_a("banana") and count_letter_a("Apple").
#
# INVESTIGATE: What does char == 'a' do when char is 'A'? Try printing
#              both and comparing. Why does case matter here?
# ==============================================================================

def count_letter_a(text):
    count = 0
    text = text.lower()
    for char in text:
        if char == 'a':
            count += 1    
    return count


# MODIFY -----------------------------------------------------------------------
# The function below only counts LOWERCASE vowels. A word like "Eagle" would
# only get 1 counted instead of 2.
#
# Fix it so it counts both uppercase and lowercase vowels.
#
# Hint: think about what you could do to `char` before you check it.
# ------------------------------------------------------------------------------

def count_vowels(text):
    text = text.lower()
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:      # ← this only matches lowercase
            count += 1
    return count


# MAKE -------------------------------------------------------------------------
# Complete this function so it returns True if EVERY character in the string
# is a digit (0–9), and False if any character is not.
#
# Examples:
#   is_all_digits("12345")  →  True
#   is_all_digits("123a5")  →  False
#   is_all_digits("")       →  True  (no characters to fail the check)
#
# Hint: char.isdigit() returns True if char is a digit character.
# ------------------------------------------------------------------------------

def is_all_digits(text):
    # TODO: loop through the string and check each character
    for char in text:
        if not char.isdigit():
            return False
    return True



# ==============================================================================
# ACTIVITY 3: String methods — .upper(), .split(), .strip(), .replace()
# ==============================================================================
#
# Before completing the tasks below, run snippet_examples.py snippets 9–12
# if you haven't already — they demonstrate each of these methods.
#
# PREDICT: What will each of these return?
#   "  hello world  ".strip()
#   "hello world".split(" ")
#   "hello world".replace("world", "Python")
#   "hello".upper()
#
# RUN: Try them in the shell (or add print() calls below).
#
# INVESTIGATE: What does "a,b,,c".split(",") return?
#              What does "hello world".split() return (no argument)?
# ==============================================================================


# MODIFY -----------------------------------------------------------------------
# The function below is supposed to remove all spaces from a string,
# but it contains a bug — it does the opposite of what it should.
#
# Example:
#   remove_spaces("hello world")  should return  "helloworld"
#
# Find and fix the bug. There is only ONE line that needs changing.
# ------------------------------------------------------------------------------

def remove_spaces(text):
    result = ""
    for char in text:
        if char == ' ':
            result = result + text.replace(char, "")  # ← this line has the bug
    return result


# MAKE -------------------------------------------------------------------------
# Complete this function so it creates an acronym from a phrase.
# Take the first letter of each word and join them together in uppercase.
#
# Examples:
#   make_acronym("North Atlantic Treaty Organisation")  →  "NATO"
#   make_acronym("as soon as possible")                →  "ASAP"
#
# Hint: use .split() to break the phrase into a list of words, then loop
#       through the list and collect the first character of each word.
# ------------------------------------------------------------------------------

def make_acronym(phrase):
    # TODO: split the phrase into words, then build the acronym
    phrase = phrase.split(" ") #split into a list
    acronym = ""
    for i in range(len(phrase)):
        acronym += phrase[i][0].upper()
    return acronym


    


# ==============================================================================
# ACTIVITY 4: Slicing and building — creating new strings from existing ones
# ==============================================================================
#
# Before starting, look at snippets 4–6 in snippet_examples.py to remind
# yourself how slicing works.
#
# PREDICT: What will these return?
#   "Python"[0]
#   "Python"[:3]
#   "Python"[2:5]
#   "Python"[-1]
#
# RUN: Check your predictions.
#
# INVESTIGATE: Try reverse_string("racecar"). What's special about it?
#              Can you work out why the loop builds the string that way?
# ==============================================================================

def reverse_string(text):
    """Builds a reversed version of text by adding each character to the front."""
    result = ""
    for char in text:
        result = char + result      # adds to the FRONT, not the back
    return result


# MAKE -------------------------------------------------------------------------
# Complete this function so it creates a username from a full name.
# Format: first letter of first name + full last name, all lowercase.
#
# Examples:
#   create_username("Zara Sharma")   →  "zsharma"
#   create_username("Ada Lovelace")  →  "alovelace"
#
# Steps to think about:
#   1. How do you split the full name into first and last?
#   2. How do you get just the first letter of the first name?
#   3. How do you join them and make it lowercase?
# ------------------------------------------------------------------------------

def create_username(full_name):
    # TODO: build the username using slicing and string methods
        full_name = full_name.lower().split(" ")
        the_full_name = full_name[0][0]
        for i in range(1, len(full_name)):
            the_full_name += full_name[i]
        return the_full_name
    


# ==============================================================================
# EXTENSION CHALLENGES
# ==============================================================================
# These are for anyone who has finished the main activities and wants to push
# further. There are no hints — work it out between you.
# ==============================================================================

# CHALLENGE 1 ------------------------------------------------------------------
# Write a function that checks whether a string is a palindrome.
# A palindrome reads the same forwards and backwards.
#
# Examples:
#   is_palindrome("racecar")  →  True
#   is_palindrome("hello")    →  False
#   is_palindrome("Level")    →  True   (case-insensitive)

def is_palindrome(text):
    new_word = ''
    for char in text:
        new_word = char + new_word
    return text == new_word # true if they are the same, false if not

print(is_palindrome("hello"))
print(is_palindrome("ada"))


# CHALLENGE 2 ------------------------------------------------------------------
# Write a function that converts camelCase to snake_case.
#
# Examples:
#   to_snake_case("myVariableName")   →  "my_variable_name"
#   to_snake_case("helloWorld")       →  "hello_world"



def to_snake_case(text):
    new_string = ""
    for char in text:
        if char.isupper():
            new_string += "_"
            new_string += char.lower()
        else:
            new_string += char
    return new_string
print(to_snake_case("MyVariableName"))


# CHALLENGE 3 ------------------------------------------------------------------
# Write a simple text analyser. Given a string of text, return a dictionary
# with these three keys:
#   "words"            →  total word count
#   "characters"       →  total character count (excluding spaces)
#   "avg_word_length"  →  average word length (rounded to 1 decimal place)
#
# Example:
#   analyse_text("I love Python")
#   →  {"words": 3, "characters": 11, "avg_word_length": 3.7}

def analyse_text(text):
    
    


# ==============================================================================
# RUN YOUR FUNCTIONS HERE
# ==============================================================================
# Add calls to your functions below. This section runs when you execute
# the file with: python exercises.py
# ==============================================================================

if __name__ == "__main__":

    print("=== Activity 1: Iterating ===")
    # print_each_character("hi there")
    # print()
    # print_with_positions("hello")       # fix this above first
    # print()
    # print(string_length_manual("hello")) # complete this above first
    # print()

    # print("\n=== Activity 2: Searching ===")
    # print(count_letter_a("banana"))
    # print(count_letter_a("Apple"))
    # print(count_vowels("Eagle"))        # should be 2 after your fix
    # print(is_all_digits("12345"))       # complete this above first
    # print(is_all_digits("123a5"))
    # print(is_all_digits(""))

    # print("\n=== Activity 3: String methods ===")
    # print(remove_spaces("hello world")) # fix the bug above first
    # print(make_acronym("North Atlantic Treaty Organisation"))

    # print("\n=== Activity 4: Slicing and building ===")
    # print(reverse_string("racecar"))
    # print(create_username("Ada Lovelace"))  # complete this above first
