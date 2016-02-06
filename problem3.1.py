def largest_prime_factor(n):

    largest_factor = 1

    # remove any factors of 2 first
    while n % 2 == 0:
        largest_factor = 2
        n = n/2

    # now look at odd factors
    p = 3
    while n != 1:
        while n % p == 0:
            largest_factor = p
            n = n/p
        p += 2

    return largest_factor

print largest_prime_factor(600851475143)
