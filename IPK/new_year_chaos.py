#!/bin/python3

import math
import os
import random
import re
import sys
import collections

def minimumBribes(q, n):
    nums = q
    another_pass = True
    counts = collections.defaultdict(int)
    
    while another_pass:
        another_pass = False
        for i, num in enumerate(q):
            if nums[i] == i + 1:
                pass
            elif i + 1 < n and nums[i+1] > nums[i]:
                another_pass = True
            else:
                counts[nums[i]] += 1
                if counts[nums[i]] > 2:
                    print("Too chaotic")
                    return
                nums[i], nums[i+1] = nums[i+1], nums[i]
    print(sum(counts.values()))
    return
                    
    

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q, n)
