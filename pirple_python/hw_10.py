"""
One of my favourite and most commonly used libs - doctest
https://docs.python.org/3/library/doctest.html

For example let's write some code to calculate Standard Deviation (SD) and check
does the code works fine
"""

# First import doctest module
import doctest

# Then create all the inner logic of the code
import math

# Calculate mean using fsum()

def calc_mean(x:int, num_list:list) -> float:
    num_sum = math.fsum(num_list)
    mu = num_sum / x
    return(mu)


# Create a SD function using math metods (pow, fsum, sqrt)
# We use func documentation part to create some examples of the func's propper work that looks like interactive sessions
# The doctest library will find them end test them (I use numpy.std func to find out true values)

def calc_sd(x:int, num_list:list) -> float:
    """
    >>> calc_sd(10, [0.3251074697680941, 0.6226290916100162,\
    0.5192710841861464, 0.42569037938461607, 0.9944647281037957,\
    0.8875197245393107, 0.18173244707909164, 0.7812581083104324,\
    0.8942831650913973, 0.35729018402756385])
    0.26543366667015483
    >>> calc_sd(8, [0.9989499714269882, 0.07704768777678506,\
    0.9658244050088403, 0.4541844337366412, 0.9551574964300932,\
    0.7689654575344405, 0.7732694392051974, 0.10595175987473338])
    0.3544927113034824
    """
    mu = calc_mean(x, num_list)
    calc_diff = [math.pow((x_i - mu), 2) for x_i in num_list]
    tot_diff = math.fsum(calc_diff)
    sigma = math.sqrt(tot_diff / x)
    return(sigma)


# Then code a test part using testmod from doctest basic API
# if everything is fine it wouldn't create any output to your session after running the code
if __name__ == '__main__':
    doctest.testmod()