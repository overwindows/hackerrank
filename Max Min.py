#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    l = len(arr)
    cur = 10**9
    for i in range(l-k+1):
        _min = arr[i+k-1] - arr[i]
        if _min == 0:
            return 0
        if _min < cur:
            cur = _min
    return cur

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
