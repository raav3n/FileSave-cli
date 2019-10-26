#!/usr/bin/env python3
import os
import getpass

from .infomodule import info

class hide():
    def __init__(self, folder_name):
        #allows only sudo
        os.system('sudo chown root {}'.format(folder_name))

        #removes access to users, groups, and others
        os.system('chmod ugo-rwx {}'.format(folder_name))

        #hides folder
        os.system('sudo chflags hiiden {}'.format(folder_name))

        #open info() to save pass and number
        info()
