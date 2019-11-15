#!/usr/bin/env python3
import os
import json
import getpass

from .showmodule import show

#foundation for show() to revert hide()
def reveal(folder_name):

    #variables
    user = ''
    folder_info = {
        'token' : '',
        'folder' : '',
        'pass_enc' : '',
        'number_contact' :'',
    }
    d = '%s/user/data.txt' % (os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

    #checks that data.txt is not empty
    if os.stat(d).st_size != 0:

        #opens data.txt file
        with open(d, 'rb') as json_file:
            data = json.load(json_file)
            for name in data:

                #loops through objects to find folder
                if data[name][0]['folder'] == folder_name:

                    #assures that folder exists in data.txt
                    user = folder_name

                    #saves items of object into folder_info
                    folder_info['token'] = data[name][0]['token']
                    folder_info['folder'] = data[name][0]['folder']
                    folder_info['pass_enc'] = data[name][0]['pass']
                    folder_info['number_contact'] = data[name][0]['number_contact']

        #prompts user if the folder is hidden already or does not exist     due to lines above
        if user == '':
            print("That folder does not exist or is not hidden.")
        else:

            #now calls for show()
            show(folder_info['token'], folder_info['folder'], folder_info['pass_enc'], folder_info['number_contact'])
    else:

        #if data.txt is empty then prompt that no folders have been hidden
        print('Nothing has been hidden...')
