#!/usr/bin/env python3
import smtplib
import os
import random

#step process that messages user via text a code they must verify
def verification(phone, carrier):
    userinfo = phone + carrier
    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP( "smtp.gmail.com", 587 )

    #generates reandom number for code
    code_gen = int((random.random()) * 1000000)

    #code gen
    code = 'Subject:Filesave Code: {}'.format(code_gen)

    server.starttls()

    server.login( 'EMAIL', 'PASS' )

    # Send text message through SMS gateway of destination number
    server.sendmail('FileSave', userinfo, code)

    #prompt user to enter code that was messaged to them
    code_in = raw_input('Please enter code sent (may take 1-2 minutes): ')

    #if user inputs code incorrectly they get options fo trying again, getting new code or quitting program
    while code_gen != int(code_in):

        #prompts user options
        option = raw_input('Sorry that was incorrect. Would you like to\nA)Try again\nB)Get a new code\nC)Cancel\n').upper()

        #option 'A' selected to try again
        if option == 'A':

            #prompts user to attempt to put code again
            code_in = raw_input('Please input code: ')

        #option 'B' was selected to call verificaiton() and get new code
        elif option == 'B':

            #calls verification() once again for new code
            verification(phone, carrier)

            #prompts user to enter new code
            code_in = raw_input("Please enter new code: ")

        #option 'C' was selected to quit promgram
        elif option == 'C':
            print("Try again, later :/")
            quit()
