#!/bin/python3

import math
import os
import random
import re
import sys
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# Complete the minimumSwaps function below.


def minimumSwaps(arr):
    # Selection sort algorithm: https://miro.medium.com/max/551/1*OA7a3OGWmGMRJQmwkGIwAw.gif
    def _swap(i,j):
        arr[i], arr[j] = arr[j], arr[i]

    count = 0
    for i in range(len(arr)-1):
        if arr[i] != i+1:
            for j in range (i+1, len(arr)):
                if arr[j] == i+1:
                    _swap(i,j)
                    count += 1
    return(count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
