#!/usr/bin/env python3
"""
Author : stanlito_15 <stanlito_15@localhost>
Date   : 2022-06-20
Purpose: howler challenge
"""

import argparse,os,io,sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='howler uppercases or lower cases an input',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        type= str,
                        help='Input str or filename')

    parser.add_argument('-o',
                        '--outdir',
                        help='output file(s)names',
                        metavar='file',
                        nargs= "*",
                        )


    parser.add_argument('-l',
                        '--lower',
                        help='stores a lower flag',
                        action='store_true')

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

    out_fh = []
    if args.outdir:
        for fh in args.outdir:
            out_fh = open(fh,"wt")  
            for line in args.text:
                if args.lower:
                    out_fh.write(line.lower())
                else:
                    out_fh.write(line.upper())
            
    else: 
        out_fh =sys.stdout
        for line in args.text:
            if args.lower:
                out_fh.write(line.lower())
            else:
                out_fh.write(line.upper())     
    out_fh.close()


  


# --------------------------------------------------
if __name__ == '__main__':
    main()
