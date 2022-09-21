#!/usr/bin/env python3
"""
Author : stanlito_15 <stanlito_15@localhost>
Date   : 2022-06-20
Purpose: low memory Howler
"""

import argparse,os,io,sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler upper cases input text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type= str,
                        help='Input str or filename')

    parser.add_argument('-o',
                        '--outfile',
                        help='output filename',
                        metavar='str',
                        type=str,
                        default='')

    

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text)
    else:
        args.text = io.StringIO(args.text + "\n")
    
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    out_fh = open(args.outfile,"wt") if args.outfile else sys.stdout
    for line in args.text:
        out_fh.write(line.upper())
    out_fh.close()



# --------------------------------------------------
if __name__ == '__main__':
    main()
