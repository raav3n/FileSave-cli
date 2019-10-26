#!/usr/bin/env python3
from cryptography.fernet import Fernet

class info():
    user_pass = input('Enter create safe password: ')
    user_pass_verify = input('Enter password once more: ')

    #run until password is typed correctly twice
    while user_pass != user_pass_verify:
        user_pass = input('You made a mistake/nPlease create password: ')
        user_pass_verify = input('Enter password once more: ')
    else:
        encrypt_pass(user_pass)
        two_auth = input('Would you like to set up a two step authentication? (y or n): ')
        if two_auth == 'y':
            phone_two_auth()
        else:
            continue

    #sets up two step auth
    def phone_two_auth():
        




    #encrypts password and phone to move to file
    def encrypt_pass():
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        cipher_text = cipher_suite.encrypt(user_pass,)




#plain_text = cipher_suite.decrypt(cipher_text)
