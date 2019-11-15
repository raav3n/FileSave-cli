#!/usr/bin/env python3
import sys
from hiddenmodule import hide
from revealmodule import reveal

def main():
    #call hide()
    if sys.argv[1] == 'hide':
        hide(sys.argv[2])
    #call show()
    elif sys.argv[1] == 'show':
        reveal(sys.argv[2])
    else:
        print("Sorry that file or funciton does not exist.")
if __name__ == '__main__':
    main()
