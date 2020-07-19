
#import the datetime class from the datetime module
from datetime import datetime



def BirthDate():
    #Create a variable to contain the current year
    year = datetime.now().year

    #ask for  user's age
    age = input('How old are you?')
    #ask user's birth month
    birth_month = input('What month is your birthday?')
    #ask user's birth day
    birth_day = input('What day of the month is your birthday?')

    #find user's birth year by subtracting current age from current year
    birth_year = year - int(age)

    statement = 'Your birth date is {} {} {}'
    print(statement.format(str(birth_day), str(birth_month), str(birth_year)))




BirthDate()
