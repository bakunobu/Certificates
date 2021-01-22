import doctest
from typing import Union


def are_two_equal(a:int, b:int, c:int) -> bool:
    """
    >>> are_two_equal(5, 6, 7)
    False
    >>> are_two_equal(5, 6, 6)
    True
    >>> are_two_equal(6, 5, 6)
    True
    >>> are_two_equal(6, 6, 5)
    True
    """
    if a == b:
        return(True)
    elif b == c:
        return(True)
    elif a == c:
        return(True)
    else:
        return(False)


# extra_credit
def multi_type_comparison(a:Union[int, str],
                          b:Union[int, str],
                          c:Union[int, str]) -> bool:
    """
    >>> multi_type_comparison(5, 6, '6')
    True
    >>> multi_type_comparison(5, 6, '7')
    False
    >>> multi_type_comparison('5', 6, 6)
    True
    >>> multi_type_comparison(6, '5', 6)
    True
    >>> multi_type_comparison(6, 6, 5)
    True
    """
    a = int(a)
    b = int(b)
    c = int(c)
    return(are_two_equal(a, b, c))

if __name__ == '__main__':
    doctest.testmod()
    
