#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = tuple(map(int, input("Enter integers: ").split()))

    for i in range(len(A) - 1, 1, -1):
        if A[i] == A[i - 1] and A[i] % 2 == 0:
            e = i
            print(A[:e])
            break
        else:
            print("There are no pairs", file=sys.stderr)
        exit(1)

