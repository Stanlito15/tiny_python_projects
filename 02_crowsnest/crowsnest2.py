#!/usr/bin/env python3
"""
Author : stanlito_15 <stanlito_15@localhost>
Date   : 2022-04-10
Purpose: Say what you see from the crowsnest
"""

import argparse
from ctypes.wintypes import WORD


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's net -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='word', help='A word')

    parser.add_argument('-s',
                        '--side',
                        type=str,
                        metavar= 'side',
                        default="larboard",
                        help='name the side of the ship')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    side = args.side
    char = word[0]
    article = ""

    if char.isupper() == True:
        if char[0] in "AEIOU":
            article = "An"
        else:
            article = "A"
    else:
        if word[0].lower() in "aeiou":
            article = "an"
        else: article = "a"
    print(f"Ahoy, Captain, {article} {word} off the {side} bow!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
