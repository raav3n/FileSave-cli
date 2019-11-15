#!/usr/bin/env python3
import os
import json
from cryptography.fernet import Fernet
from twostepmodule import verification

#show() reverts hide() by unhiding folder and deleting from data.txt
def show(token, folder_name, pass_temp, pnumber):

    #path for data.txt
    d = '%s/user/data.txt' % (os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

    #prompt user if they wish to continue with reverting hide()
    user_in = raw_input('Would you like to proceed in revealing %s? (y or n): ' % folder_name ).upper()

    #user wished to contine and it will revert hide()
    if user_in == 'Y':

        #counter for incorrectly inputted password
        count = 0

        #makes variables from json strings
        key = json.dumps(token)
        tk = json.dumps(pass_temp)

        #byte to decrpyt password
        decipher_suite = Fernet(key)

        #decrpyts password
        access = decipher_suite.decrypt(tk)

        #asks user to enter password they created in hide()
        user_pass = raw_input('\nPlease enter password: ')

        #if user inputs password incorrectly they have 4 chances
        while user_pass != access:

            #counter for chances
            count += 1

            #if user exceeds chances then program will quit
            if count == 4:
                print('Too many failed attempts.')
                quit()

            #prompts user to attempt to enter password again
            user_pass = raw_input('You made a mistake\nPlease enter password again: ')

        #Text verification is sent if it was set up, and/or reverts hide()
        else:
            
            #Runs through 2step verification to check if user set that up
            #P.S pnumber would equal '0' if user didnt set up 2step
            if pnumber != '0':

                #splits number and carrier into ver list
                ver = pnumber.split('@')

                #sets phone equal to phone number
                phone = ver[0]

                #sets carrier equal to carrier and adds '@' once again
                carrier = '@' + ver[1]

                #calls verification for 2step
                verification(phone, carrier)

            #removes access to users, groups, and others
            os.system('sudo chmod ugo+rwx {}'.format(folder_name))

            #hides folder
            os.system('sudo chflags nohidden {}'.format(folder_name))

            list = {}

            #opens data.txt
            with open(d, 'rb') as json_file:
                data = json.load(json_file)
                for name in data:

                    #checks for different folder names to save to new list
                    if data[name][0]['folder'] != folder_name:
                        list[data[name][0]['folder']] = []

                        #adds other folders to new list with elements
                        list[data[name][0]['folder']].append(data[name][0])

            #opens data.txt
            with open(d, 'wb') as outfile:

                #copys new list to data.txt it remove current folder from json
                json.dump(list, outfile)
