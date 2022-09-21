#!/usr/bin/env python3
"""
Author: Stanley Yaw Appiah <appstan2003@gmail.com>
Purpose: Say Hello
"""

import argparse


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description="Say Hello")
    parser.add_argument("-n", '--name', metavar="name",
                        default='World', help="name to greet")
    return parser.parse_args()


def main():
    """ We run the main program here"""
    args = get_args()

    print("Hello, " + args.name + '!')


if __name__ == "__main__":
    main()
