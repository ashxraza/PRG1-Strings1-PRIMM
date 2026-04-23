# Learning Strings with PRIMM

Strings are sequences of characters, which makes them a great way to practise
loops, indexing, and building new values from existing ones. This lesson uses
the **PRIMM methodology**:

| Step | What you do |
|---|---|
| **Predict** | Read the code and write down what you think it will do |
| **Run** | Execute it and check your prediction |
| **Investigate** | Try different inputs and dig into *why* it behaves that way |
| **Modify** | Fix a bug or extend the function as instructed |
| **Make** | Write your own function from scratch |

---

## Files in this repo

| File | Purpose |
|---|---|
| `snippet_examples.py` | Short warm-up snippets shown on the projector |
| `exercises.py` | Your main working file — four activities plus extension challenges |

---

## What each activity covers

**Activity 1 — Iterating over strings**
How to step through a string character by character using a `for` loop, and
how to use `range(len(...))` when you also need the index.

**Activity 2 — Searching strings**
Looking at characters one by one to count or check things. Introduces the
pattern of building a counter inside a loop.

**Activity 3 — String methods**
Using built-in methods: `.upper()`, `.lower()`, `.strip()`, `.replace()`,
and `.split()`. Covers chaining methods together.

**Activity 4 — Slicing and building**
Getting parts of a string with `[start:end]` notation, and building new
strings by accumulating characters.

**Extension challenges** *(if you finish early)*
Palindrome checker, camelCase to snake_case converter, and a text analyser.

---

## Getting started

1. Open `exercises.py` and work through the activities in order.
2. Run the file at any point with:
   ```bash
   python exercises.py
   ```
3. The bottom of `exercises.py` has a test section — you will see errors or
   `None` values for any function you have not completed yet. That is normal.

---

## Key concepts to leave with

- Strings are sequences — you can loop over them and index into them just
  like lists
- `string[i]` gives you one character; `string[start:end]` gives you a slice
- String methods (`.split()`, `.strip()`, `.replace()`, etc.) do not change
  the original string — they return a new one
- The accumulation pattern (building up a result string inside a loop) is
  used constantly in real Python code

---

## Additional resources

- [Python docs — Strings](https://docs.python.org/3/tutorial/introduction.html#strings)
- [Python docs — String methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Real Python — Strings and character data](https://realpython.com/python-strings/)
