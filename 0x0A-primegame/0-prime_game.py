#!/usr/bin/python3
''' Prime Game Module '''


def isWinner(x, nums):
    ''' Return the winner
    '''
    if x < 1 or not nums:
        return None

    maria, ben = 0, 0
    # Since Maria always plays first, she only wins when
    # the number of prime numbers available is prime
    for num in nums:
        print(primeNumbers(num))
        if len(primeNumbers(num)) % 2 == 0:
            ben += 1
            print('Ben win')
            continue
        maria += 1
        print('Maria win')

    if maria == ben:
        return None
    return 'Maria' if maria > ben else 'Ben'


def primeNumbers(n):
    '''
        Returns a list of prime numbers between 2 and n.
    '''
    prime_list = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, num)):
            prime_list.append(num)

    return prime_list
