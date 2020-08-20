#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    s1 = sum(h1)
    s2 = sum(h2)
    s3 = sum(h3)
    h = 0
    while(not(s1==0 or s2==0 or s3==0)):
        if(s1==s2 and s2==s3 ):
            return s1
        if(s1>=s2 and s1>=s3):
            h=h1.pop(0)
            s1-=h
        elif(s2>=s1 and s2>=s3):
            h=h2.pop(0)
            s2-=h
        else:
            h=h3.pop(0)
            s3-=h
    return 0       
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
