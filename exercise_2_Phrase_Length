# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.
prompt = "Please enter a word or phrase> Enter 'quit' to end session: "
char = input(prompt)

while char != "quit":
    while char.isalpha() == False:
        char = input(prompt)    
    print(char + " is " + str(len(char)) + " characters long.")
    char = input(prompt)
print("Goodbye!")