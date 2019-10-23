#!/bin/python3
# Source: https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def bubble_sort(q) -> int:

    def _swap(q,x):
        tmp = q[x]
        q[x] = q[x+1]
        q[x+1] = tmp

    def _check_caotic(q):
        for i in range(len(q)-1):
            if i+1 < q[i+1] < i+3:
                return True

    #if _check_caotic(q):
    #    return "Too chaotic"
    result=0
    c_swaps=-1
    while (c_swaps != 0):
        c_swaps = 0
        for i in range(len(q)-1):
            if q[i] > q[i+1]:
                _swap(q,i)
                c_swaps += 1
                result += 1
    print(" ".join(map(str,q)))
    return(result)
# END bubble_sort
    

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))
        
        print(bubble_sort(q))
# END main
