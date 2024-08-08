#!/usr/bin/python3
"""script to test minoperatiions"""


if __name__ == "__main__":
    minOperations = __import__('0-minoperations').minOperations

    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
 
    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
