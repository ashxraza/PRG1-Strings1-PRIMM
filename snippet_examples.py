# ------------------------------------------------------------------------------
# SECTION 1: Indexing — getting one character by position
# ------------------------------------------------------------------------------

# Snippet 1 — What does [0] give you?
name = "Ada Lovelace"
print(name[0])

# Snippet 2 — Negative indexes count from the end
name = "Ada Lovelace"
print(name[-1])

# Snippet 3 — What happens if you use an index equal to the length?
name = "Ada Lovelace"
print(name[3])


# ------------------------------------------------------------------------------
# SECTION 2: Slicing — getting a chunk of characters
# ------------------------------------------------------------------------------

# Snippet 4 — Slice from the start
text = "Gaming is relaxing"
print(text[:6])

# Snippet 5 — Slice to the end
text = "Gaming is relaxing"
print(text[10:])

# Snippet 6 — Negative slice from the end
text = "Gaming is relaxing"
print(text[-8:])


# ------------------------------------------------------------------------------
# SECTION 3: Iterating — stepping through a string character by character
# ------------------------------------------------------------------------------

# Snippet 7 — Loop directly over the string
name = "Ada Lovelace"
for char in name:
    print(char)

# Snippet 8 — Loop using range and index
name = "Ada"
for i in range(len(name)):
    print(i, name[i])


# ------------------------------------------------------------------------------
# SECTION 4: String methods
# ------------------------------------------------------------------------------

# Snippet 9 — .upper() and .lower()
phrase = "coding gives your brain a workout"
print(phrase.upper())

# Snippet 10 — .strip() removes whitespace from both ends
title = "  THE HANGOVER  "
print(title.strip())

# Snippet 11 — .replace() swaps one part for another
url = "www.youtube.com/watch?v=dQw4"
new_url = url.replace("youtube", "invidious")
print(new_url)

# Snippet 12 — .split() breaks a string into a list
colours = "red,blue,green"
colour_list = colours.split(",")
print(colour_list)
print(colour_list[2])


# ------------------------------------------------------------------------------
# SECTION 5: Building and formatting strings
# ------------------------------------------------------------------------------

# Snippet 13 — Concatenation with +
part1 = "Stream"
part2 = "ing is good"
print(part1 + part2)

# Snippet 14 — f-strings
game = "Cyberpunk 2077"
release_year = 2020
print(f"My favourite game is {game}, released in {release_year}.")

# Snippet 15 — Chaining methods
user_input = " I love python! "
cleaned = user_input.strip().replace("love", "♥").capitalize()
print(cleaned)
