#!/usr/bin/env python3
import os
import json
import getpass

from .showmodule import show


def reveal(folder_name):
    user = ''
    folder_info = {
        'token' : '',
        'folder' : '',
        'pass_enc' : '',
        'number_contact' :'',
    }
    d = '%s/user/data.txt' % (os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


    if os.stat(d).st_size != 0:
        with open(d, 'rb') as json_file:
            data = json.load(json_file)
            for name in data:
                if data[name][0]['folder'] == folder_name:
                    user = folder_name

                    folder_info['token'] = data[name][0]['token']
                    folder_info['folder'] = data[name][0]['folder']
                    folder_info['pass_enc'] = data[name][0]['pass']
                    folder_info['number_contact'] = data[name][0]['number_contact']
        if user == '':
            print("That folder does not exist or is not hidden.")
        else:
            show(folder_info['token'], folder_info['folder'], folder_info['pass_enc'], folder_info['number_contact'])
    else:
        print('Nothing has been hidden...')
