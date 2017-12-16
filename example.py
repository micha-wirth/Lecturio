#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Main program.
"""


import  datetime
from optparse import OptionParser
import os
import sys

my_dir = os.path.dirname
sys.path.append(my_dir(my_dir(os.path.abspath(__file__))))


def main():
    """
    Main function of main program.
    :return:
    """
    today = datetime.datetime.today()
    return today


if __name__ == '__main__':
    # Only executed if condition is fullfilled.
    main()



