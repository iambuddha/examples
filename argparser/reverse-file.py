#!/usr/bin/env python3.8

import argparse
import sys

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
args = parser.parse_args()


try:
    f = open(args.filename)
    limit = args.limit
# this except only if the file not found
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(2)

# this except all possible errors
#except:
#    print(f"something wrong")

else:

    with f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:limit]

        for line in lines:
            print(line.strip()[::-1])

# finally statment is good when you need to do something after error happened
# clean up for instance
finally:
    print("Finally")
#parse the argument


# read the file, revers the contets and print


