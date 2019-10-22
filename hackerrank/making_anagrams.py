#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a_set=set(a)
    b_set=set(b)
    result=0
    for i in a_set:
        if a.count(i) > b.count(i):
            result += a.count(i) - b.count(i)
            #print(str(i)+" "+str(result))
    for j in b_set:
        if b.count(j) > a.count(j):
            result += b.count(j) - a.count(j)
            #print(str(j)+" "+str(result))

    return(result)

if __name__ == '__main__':
    #fptr = open("./output.txt",'w')

    #a = input()
    #b = input()
    a = "fcrxzwscanmligyxyvym"
    b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

    res = makeAnagram(a, b)
    print(res)

    #fptr.write(str(res) + '\n')
    #fptr.close()
