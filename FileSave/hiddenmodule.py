#!/usr/bin/env python3
import os

from .infomodule import make_pass


def hide(folder_name):
    #open info() to save pass and number
    make_pass(folder_name)

    #removes access to users, groups, and others
    os.system('sudo chmod ugo-rwx {}'.format(folder_name))

    #hides folder
    os.system('sudo chflags hidden {}'.format(folder_name))
