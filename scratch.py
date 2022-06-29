

def is_valid_day(input_str):
    if input_str.strip().isdigit():
        print("is number")
    else:
        print("is string")
        
day = input("Enter number: ")
is_valid_day(day)