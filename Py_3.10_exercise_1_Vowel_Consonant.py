# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 


letter = input("Please enter a letter from the alphabet (a-z or A-Z): ")
print(letter)

while letter.isalpha() == False:
    letter = input("Please enter a letter from the alphabet (a-z or A-Z): ")


# 2. Write the code that determines whether the letter entered is a vowel
# Could use recursion or elif statements, but I would have to look up some documentation for recursion. 
# I chose to use the python match case control flow for this solution instead of branching with if statements for readability

# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':
def is_vowel(char):

    match char:
        case "A" | "a" | "E" | "e" | "I" | "i" | "O" | "o" | "U" | "u":
            return print(f"{char} is a vowel.")
        case _:
            return print(f"{char} is a consonant.")
is_vowel(letter)