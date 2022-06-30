# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

###################
## FUNCTIONS
###################
def is_valid_day(month,str):
    is_valid = None
    if str.strip().isdigit():
        is_valid = True
    else:
        is_valid = False
    
    if str.strip().isdigit():
        num = int(str)
        match month:
            case "Apr" | "Jun" | "Sep" | "Nov":
                if num > 30:
                    is_valid = False
                else:
                    is_valid = True
            case "Feb":
                if num > 29:
                    is_valid = False
                else:
                    is_valid = True
            case _:
                if num < 1 or num > 31:
                    is_valid = False
                else:
                    is_valid = True
    return is_valid

# I could have used "if in" instead of match case.  I just wanted to test out match case in python
def calc_season(month, day):
    season = None
    match month:
        case "Dec" | "Jan" | "Feb"  | "Mar":
            season = "Winter"
            if month == "Dec":
                if day < 21:
                    season = "Fall"
            elif month == "Mar":
                if day > 19:
                    season = "Spring"
            
        case "Apr" | "May"| "Jun":
            season = "Spring"
            if month == "Jun": 
                if day > 20:
                    season = "Summer"
                
        case "Jul" | "Aug" | "Sep":
            season = "Summer"
            if month == "Sep":
                if day > 21:
                    season = "Fall"
                
        case "Oct" | "Nov":
            season = "Fall"
            
    return print(f"{month} {day} is in the {season}.")

##################
## VARIABLES
##################
user_month = None   
tuple_months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
prompt_month = ("\n*SELECT MONTH*\n\nEnter the month of the season using 3 letter abbreviation. \nExample Jan, Feb, Mar: ")
prompt_day = (f"\n**SELECT DAY** \n\nNOTE: Apr, Jun, Sep, and Nov have 30 days. \nFeb has only 28/29 days. \nEnter the day of the month: ")

######################
## VALIDATE USER INPUT
######################
user_month = input(prompt_month)
user_month = user_month.lower()
user_month = user_month.capitalize() 

while user_month != "quit":
    while not(user_month in tuple_months):        
        user_month = input(prompt_month)
        user_month = user_month.lower()
        user_month = user_month.capitalize() 
    
    day = (input(prompt_day))   

    while not(is_valid_day(user_month,day)):
        day = (input(prompt_day))

    day = int(day)

    ########################
    ## RENDER RESULT
    ########################
    print(f"\n****************************\nRESULT:")     
    calc_season(user_month, day)
    print("****************************")

    ######################
    ## PROMPT CONTINUATION
    ######################
    print("\n***ENTER 'quit' TO END***")
    user_month = input(prompt_month)
    # user_month = user_month.lower()
    # user_month = user_month.capitalize()