
import re

def validate_password(password):

    
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*!]).{8,}$'

    if re.match(pattern, password):
        print("Valid Password")
    else:
        print("Invalid Password")
        print("Password must contain:")
        print("- At least 8 characters")
        print("- At least one uppercase letter")
        print("- At least one lowercase letter")
        print("- At least one digit")
        print("- At least one special character (@#$%^&*!)")


password = input("Enter your password: ")

validate_password(password)
