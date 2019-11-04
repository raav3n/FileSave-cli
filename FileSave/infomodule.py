#!/usr/bin/env python3
from cryptography.fernet import Fernet
from twostepmodule import verification


def make_pass():
    user_carrier = ''
    user_pass = raw_input('Enter create safe password: ')
    user_pass_verify = raw_input('Enter password once more: ')

    #run until password is typed correctly twice
    while user_pass != user_pass_verify:
        user_pass = raw_input('You made a mistake\nPlease create password: ')
        user_pass_verify = raw_input('Enter password once more: ')
    else:
        #Ask to set up two step auth
        two_auth = raw_input('Would you like to set up a two step authentication? (y or n): ')
        if two_auth == 'y':
            phone_two_auth()
        # encrypt_pass(user_pass)
        print('done')

#sets up two step auth
def phone_two_auth():
    phone_carriers = {'A':'@mms.att.net', 'B':'@tmomail.net', 'C':'@vtext.com','D':'@pm.sprint.com'}

    carrier = raw_input('A)At&t\nB)T-Mobile\nC)Verizon\nD)Sprint\nWhat is your phone carrier? ').upper()
    for k,v in phone_carriers.items():
        if carrier == k:
            user_carrier = v
    else:
        print('Now please enter your number for Two-Step Verification')
        number = raw_input('Now input your phone number: ')
        temp = raw_input("Please type in the number again: ")
        while number != temp:
            print('Sorry, there was a mistake. Please try again')
            number = raw_input('Input your number: ')
            temp = raw_input('Enter number once more :')
        else:
            verification(number,user_carrier)




#encrypts password and phone to move to file
# def encrypt_pass(pass):
#     key = Fernet.generate_key()
#     cipher_suite = Fernet(key)
#     cipher_text = cipher_suite.encrypt(pass)




#plain_text = cipher_suite.decrypt(cipher_text)
