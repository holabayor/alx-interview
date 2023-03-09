#!/usr/bin/python3
''' Prime Game Module '''


def isWinner(x, nums):
    ''' Return the winner
    '''
    if x < 1 or not nums:
        return None

    maria_wins, ben_wins = 0, 0
    # Since Maria always plays first, she only wins when
    # the number of prime numbers available is prime
    for num in nums:
        if len(primeNumbers(num)) % 2 == 0:
            ben_wins += 1
            continue
        maria_wins += 1

    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'


def primeNumbers(n):
    '''
        Returns a list of prime numbers between 2 and n.
    '''
    prime_list = []

    for i in range(1, n+1):
        if n % i == 0:
            prime_list.append(i)
    return prime_list
