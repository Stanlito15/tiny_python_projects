#!/usr/bin/env python3
"""
Author : stanlito_15 <stanlito_15@localhost>
Date   : 2022-05-17
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- Choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        type=str,
                        help='A positional argument')
    parser.add_argument('-s',
                        '--side',
                        help='name the side of the ship',
                        action= "store_true")

    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    flag_side = "starboard" if args.side == True else "larboard"

    article = ""
    if word[0].isupper() == True:
        if word[0] in "AEIOU":
            article = "An"
        else:
            article = "A"
    else:
        if word[0].lower() in "aeiou":
            article = "an"
        else: article = "a"
    


    print(f'Ahoy, Captain, {article} {word} off the {flag_side} bow!')



# --------------------------------------------------
if __name__ == '__main__':
    main()
