# This was taken from lecture 16, slides 14-17
# Start with 1 in divisor tuple
# Search up to halfway point
# After for loop add number itself to tuple
# Call function
def findDivisors(num):
    """Finds divisors of number
       Notice 1 already included and number itslef added at end"""

    divisors = (1,)
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            divisors += (i,)
    divisors += (num,)
    return divisors

print(findDivisors(100))