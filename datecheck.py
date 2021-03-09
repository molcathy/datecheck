'''
Write a program which:
* inputs a date as a string in the form dd/mm/yy
* and validates it as described in the table  below:
    a) The date must be 8 characters long 
'''
date = input('Enter a date: ')
chars = 8

def isDateCharsLength(d, chars):
    if len(d) != chars:
        return False
    else:
        return True

if isDateCharsLength(date, chars) == False:
    print(f"Date not {chars} characters!")

