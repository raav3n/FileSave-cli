#!/usr/bin/env python3
import os
import getpass

from .infomodule import make_pass


def hide(folder_name):
    #removes access to users, groups, and others
    os.system('chmod ugo-rwx {}'.format(folder_name))

    #hides folder
    os.system('chflags hidden {}'.format(folder_name))

    #allows only sudo
    os.system('sudo chown root {}'.format(folder_name))

    #open info() to save pass and number
    make_pass()
