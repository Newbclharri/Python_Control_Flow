# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

term_1 = 0
term_2 = 1

for count in range(50):
    print(f"term: {count} / number: {term_2}")
    term_1, term_2 = term_2, term_1 + term_2 
    #term_1 does not update in (term_1 + term_2 expression) 
    # eventhough term_2 is assigned to term_1 on the same line
    #This makes the one-line preferred for this solultion.
