def sum_of_factors(n):
    factors_sum = sum([x for x in range(1, n) if n % x == 0])
    return factors_sum

def decide(n):
    if sum_of_factors(n) > n:
        return (f"{n} is abdundant.")
    elif sum_of_factors(n) == n:
        return (f"{n} is a perfect number.")
    elif sum_of_factors(n) < n:
        return (f"{n} is deficient.")
