#!/usr/bin/env python3
import os
import json
from cryptography.fernet import Fernet
from twostepmodule import verification

#create pass word function
def make_pass(folder):

    #variable
    user_carrier = ''
    num = 1
    data = {}
    d = '%s/user/data.txt' % (os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

    #check if folder exists, prompts error
    if os.path.isdir(folder) == False:
        print('Folder does not exist in this directory.')
        quit()

    #checks that file isn't empty
    if os.stat(d).st_size != 0:

        #open data.txt file
        with open(d,'r') as json_file:
            data = json.load(json_file)
            for name in data:

                #check data.txt if file is already hidden
                if data[name][0]['folder'] == folder:
                    print('This folder is already hidden')
                    quit()

            #num is used to continue adding objects to data.txt
            num = len(data.keys()) +1

    #user enters password
    user_pass = raw_input('Enter create safe password: ')
    user_pass_verify = raw_input('Enter password once more: ')

    #run until password is typed correctly twice
    while user_pass != user_pass_verify:

        user_pass = raw_input('You made a mistake\nPlease create password: ')
        user_pass_verify = raw_input('Enter password once more: ')

    else:

        #encrypts password created, saving key and encrypted password
        key, cipher_text = encrypt_pass(user_pass)

        #Ask to set up two step auth
        two_auth = raw_input('Would you like to set up a two step authentication? (y or n): ').upper()


    data['info' + str(num)] = []

    #if 2step was set up then it adds number to json on data.txt
    if two_auth == 'Y':
        number,user_carrier = phone_two_auth()
        data['info' + str(num)].append({
            'token': key,
            'folder': folder,
            'pass': cipher_text,
            'number_contact': (number+user_carrier),
        })

    #this is the json added if 2step was not set up
    elif two_auth == 'N':
        data['info' + str(num)].append({
            'token': key,
            'folder': folder,
            'pass': cipher_text,
            'number_contact': '0',
        })

    #Opens data.txt and copys json into file
    with open(d, 'w') as outfile:
        json.dump(data, outfile)

        print('done')

#sets up two step auth
def phone_two_auth():

    #phone carriers that can be used
    phone_carriers = {'A':'@mms.att.net', 'B':'@tmomail.net', 'C':'@vtext.com','D':'@pm.sprint.com\n'}

    #prompts user what carrier they have
    carrier = raw_input('\nA)At&t\nB)T-Mobile\nC)Verizon\nD)Sprint\nWhat is your phone carrier? ').upper()

    #gets carrier input and loops thorugh phone_carriers to find which carrier was selected
    for k,v in phone_carriers.items():
        if carrier == k:
            user_carrier = v
    else:
        print('Now please enter your number for Two-Step Verification')

        #Asks user to enter phone number
        number = raw_input('Now input your phone number: ')
        temp = raw_input("Please type in the number again: ")

        #loops user to enter phone number until they are the same
        while number != temp:
            print('Sorry, there was a mistake. Please try again')
            number = raw_input('Input your number: ')
            temp = raw_input('Enter number once more :')
        else:

            #calls verification()
            verification(number,user_carrier)

    return number, user_carrier




#encrypts password and phone to move to file
def encrypt_pass(password):
    #generates key
    key = Fernet.generate_key()

    #cipher byte is made
    cipher_suite = Fernet(key)

    #password is encrypted
    cipher_text = cipher_suite.encrypt(password)

    return key, cipher_text
