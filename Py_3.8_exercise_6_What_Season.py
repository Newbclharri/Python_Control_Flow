############################
## Py 3.8 Compatible Version
############################

#################
## FUNCTIONS
#################

def is_valid_day(month, str):
    is_valid = None
    if str.strip().isdigit():
        is_valid = True
    else:
        is_valid = False
        
    if str.strip().isdigit():
        num = int(str)
        if month in ("Apr", "Jun", "Sep", "Nov"):
            if num > 30:
                is_valid = False
            else:
                is_valid = True
        elif month in ("Feb"):
            if num > 29:
                is_valid = False
            else:
                is_valid = True
        else:
            if num < 1 or num > 31:
                is_valid = False
            else:
                is_valid = True
    return is_valid

def calc_season(month, day):
    season = None
    
    if month in ("Jan", "Feb", "Mar"):
        season = "Winter"
        if month == "Mar" and day > 19:
            season = "Spring"
    
    if month in ("Apr", "May", "Jun"):
        season = "Spring"
        if month == "Jun" and day > 20:
            season = "Summer"
    
    if month in ("Jul", "Aug", "Sep"):
        season = "Summer"
        if month == "Sep" and day > 21:
            season = "Fall"
    
    if month in ("Oct", "Nov", "Dec"):
        season = "Fall"
        if month == "Dec" and day < 21:
            season = "Winter"
                        
    print(f"{month} {day} is in the {season}.")

###############
## VARIABLES
################
user_month = None
tuple_months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
prompt_month = ("\n*SELECT MONTH*\n\nEnter the month of the season using 3 letter abbreviation. \nExample Jan, Feb, Mar: ")
prompt_day = (f"\n**SELECT DAY**\n\nNOTE: Apr, Jun, Sep, and Nov have 30 days. \nFeb has only 28/29 days. \nEnter the day of the month: ")

######################
## VALIDATE USER INPUT
######################
while user_month != "Quit":
    while not(user_month in tuple_months):
        user_month = input(prompt_month)
        user_month = user_month.lower()
        user_month = user_month.capitalize()

    day = (input(prompt_day))
    while not(is_valid_day(user_month, day)):
        day = (input(prompt_day))
    day = int(day)
    
    ################
    ## RENDER RESULT
    ################    
    print(f"\n****************************\nRESULT:")
    calc_season(user_month, day)
    print("****************************")
    
    ######################
    ## PROMPT CONTINUATION
    ######################
    print("\n***ENTER 'Quit' TO END***")
    user_month = input(prompt_month)
    user_month = user_month.lower()
    user_month = user_month.capitalize()
