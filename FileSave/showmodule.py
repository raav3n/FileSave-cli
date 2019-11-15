#!/usr/bin/env python3
import os
import json
from cryptography.fernet import Fernet
from twostepmodule import verification

def show(token, folder_name, pass_temp, pnumber):
    d = '%s/user/data.txt' % (os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    user_in = raw_input('Would you like to proceed in revealing %s? (y or n): ' % folder_name ).upper()

    if user_in == 'Y':
        count = 0
        key = json.dumps(token)
        tk = json.dumps(pass_temp)

        decipher_suite = Fernet(key)
        access = decipher_suite.decrypt(tk)

        #delete
        print(access)

        user_pass = raw_input('\nPlease enter password: ')

        while user_pass != access:
            count += 1
            if count == 4:
                print('Too many failed attempts.')
                break
            user_pass = raw_input('You made a mistake\nPlease enter password again: ')
        else:
            if pnumber != '0':
                ver = pnumber.split('@')
                print(pnumber,ver)
                phone = ver[0]
                carrier = '@' + ver[1]
                verification(phone, carrier)

            #removes access to users, groups, and others
            os.system('sudo chmod ugo+rwx {}'.format(folder_name))

            #hides folder
            os.system('sudo chflags nohidden {}'.format(folder_name))

            list = {}
            with open(d, 'rb') as json_file:
                data = json.load(json_file)
                for name in data:
                    if data[name][0]['folder'] != folder_name:
                        list[data[name][0]['folder']] = []
                        list[data[name][0]['folder']].append(data[name][0])

            with open(d, 'wb') as outfile:
                json.dump(list, outfile)
