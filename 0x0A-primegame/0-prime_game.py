#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """ Returns a list of prime numbers up to n using the Sieve of Eratosthenes. """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return primes

def isWinner(x, nums):
    """ Determines who the winner is in a series of prime games. """
    if not nums or x <= 0:
        return None
    
    # Find the maximum number in nums to generate primes up to that number
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    # Precompute the number of primes up to each number n
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)
    
    # Maria wins count, Ben wins count
    maria_wins, ben_wins = 0, 0
    
    # Process each round
    for n in nums:
        # If the number of primes up to n is odd, Maria wins; otherwise, Ben wins
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Test the function
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))  # Example test case

