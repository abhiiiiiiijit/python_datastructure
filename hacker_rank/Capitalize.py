#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s_list = s.split(' ')
    s_list = [w.capitalize() for w in s_list]
    captised_string = ' '.join(s_list)
    return captised_string.strip()



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
