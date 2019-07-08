def gcd_euclid(a, b):
    # base condition/exit condition to avoid infinite recursion
    if b == 0:
        return a

    # actual recursion to find GCD if base condition isn't met,
    # the below lines of code mainly, minimises the problem to base condition
    else:
        return gcd_euclid(b, a%b)
