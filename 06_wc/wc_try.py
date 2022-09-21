#!/usr/bin/env python3
"""
Author : stanlito_15 <stanlito_15@localhost>
Date   : 2022-06-22
Purpose: word Count challenge
"""

import argparse,sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Word count challenge',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

  
    parser.add_argument(
                        'file',
                        help='Input file(s)',
                        metavar='FILE',
                        # we modifiy the nargs to take multiple input files "*"
                        nargs="*",
                        # if  the user supplies  any arguments 
                        #argparse will check if they are valid file inputs
                        #if there is a problem
                        #argparse will halt execution of the program and show the user an error message

                        type=argparse.FileType('rt'),

                        #if you set the default to a list with sys.stdin
                        #you have handled  the STDIN option
                        default=[sys.stdin])

    parser.add_argument('-c',
                        '--characters',
                        help='show the charcters column',
                        action='store_true')

    parser.add_argument('-l',
                        '--lines',
                        help='show the lines column',
                        action='store_true')
                        
    parser.add_argument('-w',
                        '--words',
                        help='shows the words column',
                        action='store_true')
    parser.add_argument('-o',
                        '--outfile',
                        help='output filename',
                        metavar='text',
                        nargs="*",
                        default=[sys.stdout]
                        )
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    total_lines, total_words, total_bytes = 0, 0 ,0

    for fh in args.file:
        num_lines, num_words,num_bytes = 0, 0, 0

        for line in fh:
            num_lines +=1
            num_words += len(line.split())
            num_bytes += len(line)

        total_lines += num_lines
        total_words += num_words
        total_bytes += num_bytes

        print(f"{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}")

    
    if len(args.file) > 1:
        print(f"{total_lines:8}{total_words:8}{total_bytes:8} total")



         



# --------------------------------------------------
if __name__ == '__main__':
    main()
