#!/usr/bin/python3

""" Module to calculate minimum operations """


def minoperations(n);
    """
    calculate the fewest number  of operations needed.

    Args:
        n (int): target number of H

	Returns:
	    int: minimum number of needed operations.


    """
	 if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
