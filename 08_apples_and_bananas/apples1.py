#!/usr/bin/env python3
"""
Author : stanlito_15 <stanlito_15@localhost>
Date   : 2022-06-25
Purpose: Apples and Bananas Str.replace()
"""

import argparse,os
from hashlib import new


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='str',
                        type=str,
                        default='a',
                        choices=list("aeiou")
                        )


    args =  parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
   
    vowel = args.vowel

    def new_char(c):
        return vowel if c in "aeiou" else vowel.upper() if c in "AEIOU" else c
    
    text = "".join(new_char(c) for c in args.text)

    print(text)
# --------------------------------------------------
if __name__ == '__main__':
    main()
