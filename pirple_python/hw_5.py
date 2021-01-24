import doctest

def is_prime(x:int) -> bool:
    """
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(9)
    False
    >>> is_prime(17)
    True
    >>> is_prime(27)
    False
    """
    primes = []
    nums = list(range(2, x+1))
    while nums:
        i = nums.pop(0)
        nums = [x for x in nums if x % i != 0]
        primes.append(i)
    if x in primes:
        return(True)
    else:
        return(False)


def fizz_buzz() -> None:
    for x in range(1, 101):
        if not x % 3 and not x % 5:
            print('FizzBuzz')
        elif not x % 3:
            if is_prime(x):
                print('Fizz', 'Prime')
            else:
                print('Fizz')
        elif not x % 5:
            if is_prime(x):
                print('Buzz', 'Prime')
            else:
                print('Buzz')
        elif is_prime(x):
            print('Prime')
        else:
            print(x)

    
if __name__ == '__main__':
    doctest.testmod()
    
    
