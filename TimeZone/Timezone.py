
#import the datetime class from the inbuilt datetime module
from datetime import datetime

#after pip-installing the pytz(python time zone) module,
#import the timezone class
from pytz import timezone

# format = "%Y-%m-%d %H:%M:% %z"
try:
    # welcome worker
    def welcome():
        print('''
        Welcome to use the time zone checker
        ''')


    #timeCheckerFunction
    def timeChecker():
        branch = input('''
        WeTech Solutions has two branches in addition to the current branch in Accra, Ghana.
        One in Sidney, Australia and the other in Michigan, US
        Please type in the time zones of the branch you will like to check;
        1 for Michigan, US
        2 for Sidney, Australia
        
        ''')

        #Show user current time
        currentTime = datetime.now(timezone('UTC'))
        print(f"Your current time is {currentTime}")

        #1 for Time in Michigan/Us

            
        if branch == '1':
            usbranch_time = currentTime.astimezone(timezone('US/Michigan'))
            print(f"WeTech US/Michigan branch time is {usbranch_time}")
        
        #2 for Time in Sydney/Australia
        elif branch == '2':
            australiabranch_time = currentTime.astimezone(timezone('Australia/Sydney')) 
            print(f"WeTech Sidney/Australia branch time is {australiabranch_time}")

except: 
    print('Type 1 or 2')


welcome()
timeChecker()
