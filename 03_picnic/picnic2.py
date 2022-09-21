#!/usr/bin/env python3
"""
Author : stanlito_15 <stanlito_15@localhost>
Date   : 2022-05-23
Purpose: Picnic Game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs="+",
                        help='Item(s) to bring')


    parser.add_argument('-s',
                        '--sorted',
                        help="sort the items",
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    num = len(items)

    if args.sorted == True:
        items.sort()
    
    bringing =""

    if num == 1:
        bringing = items[num-1]
    elif num ==2:
        bringing = ' and '.join(items)   
    else:
        items[-1] = 'and '+ items[-1]
        bringing=", ".join(items)
        
    print(f"You are bringing {bringing}.")



# --------------------------------------------------
if __name__ == '__main__':
    main()
