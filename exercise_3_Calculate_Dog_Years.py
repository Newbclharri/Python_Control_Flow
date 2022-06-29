# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

prompt = "Enter your dog's age in human years: "
remaining_yrs = None
dog_age_dog_yrs = None

dog_age_human_yrs = int(input(prompt))

while dog_age_human_yrs < 1:
    dog_age_human_yrs = int(input(prompt))
    
if dog_age_human_yrs >= 2:
    remaining_yrs = dog_age_human_yrs - 2
    dog_age_dog_yrs = 20 + (remaining_yrs*7)
else:
    dog_age_dog_yrs = dog_age_human_yrs * 10
    
print(dog_age_dog_yrs)
