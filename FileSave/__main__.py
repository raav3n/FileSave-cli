#!/usr/bin/env python3
import sys
from hiddenmodule import hide
from revealmodule import reveal

def main():
    # print('in main')
    # args = sys.argv[1:]
    # print('count of args :: {}'.format(len(args)))
    # print(sys.argv)
    # for arg in args:
    #     print('passed argument :: {}'.format(arg))
    # my_function('hello world')
    # my_object = MyClass('Thomas')
    # my_object.say_name()
    if sys.argv[1] == 'hide':
        hide(sys.argv[2])
    elif sys.argv[1] == 'show':
        reveal(sys.argv[2])
    else:
        print("Sorry that file or funciton does not exist.")
if __name__ == '__main__':
    main()
