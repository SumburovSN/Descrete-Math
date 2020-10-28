def is_prime(integer):
    limit = round(integer/2) + 2
    for i in range(2, limit):
        if integer % i == 0:
            return False
    return True


def get_prime(start):
    prime = start
    while not is_prime(prime):
        prime += 1
    return prime


def build_factors(number):
    factors = []
    for factor in range(2, number + 1):
        if number % factor == 0:
            factors.append(factor)
    return factors


def build_coprime(basic):
    coprimes = []
    factors_basic = build_factors(basic)
    for coprime in range(3, basic):
        factors_coprime = build_factors(coprime)
        for factor in factors_coprime:
            if factor in factors_basic:
                break
        else:
            coprimes.append(coprime)
    return coprimes


def get_congruent(coefficient, remainder0, modulo):
    remainder = remainder0
    if remainder0 > modulo:
        remainder = remainder0 % modulo
    for congruent in range(modulo + 1):
        if (coefficient * congruent) % modulo == remainder:
            return congruent
    return "Failure"


def euclidean(a, b):
    """
    :return greatest common divisor of integrals a and b
    """
    while True:
        r = a % b
        if r == 0:
            return b
        else:
            a = b
            b = r


def hidden_number(p0, q0):
    p = get_prime(p0)
    print("p = {}".format(p))
    q = get_prime(q0)
    print("q = {}".format(q))
    n = p*q
    print("n = {}".format(n))
    z = (p - 1)*(q - 1)
    print("z = {}".format(z))
    print(build_coprime(z))
    k = int(input("Choose k from the set above:"))
    # k = 3
    print("k = {}".format(k))
    j = get_congruent(k, 1, z)
    print("j = {}".format(j))
    print("j * k = {}".format(j * k))
    P = int(input("Input number to hide:"))
    P_in_k = pow(P, k)
    print("P^k = {}".format(P_in_k))
    P_rem_n = P % n
    print("P%n = {}".format(P_rem_n))
    P_rem_n_pow_k = pow(P_rem_n, k)
    print("(P%n)^k = {}".format(P_rem_n_pow_k))
    P_pow_k_rem_n = P_rem_n_pow_k % n
    print("((P%n)^k) % n = {}".format(P_pow_k_rem_n))
    E = P_pow_k_rem_n
    # E = P_in_k % n
    print("E = {}".format(E))

    E_pow_j_rem_n = pow(E % n, j) % n
    E_in_j = pow(E, j)
    print("E^j = {}".format(E_in_j))
    P = E_pow_j_rem_n
    print("P = {}".format(P))
    return P

# hidden_number(183, 151)
# hidden_number(61, 53)
# hidden_number(5, 7)
# hidden_number(7, 13)

print(euclidean(1071, 462))
print(euclidean(462, 2142))

# print(get_congruent(7, 12, 13))
# print(get_congruent(3, 12, 5))
# print(get_congruent(84, 117, 15))
# print(get_congruent(20, 23, 14))
# print(get_congruent(3, 2, 6))
# print(get_congruent(2, 8, 3))
# print(get_congruent(3, 12, 4))
# print(get_congruent(3, 2, 5))
# print(build_factors(83))


# print(get_prime(1234567))
# print(get_coprime(9812345))
# print(build_factors(1025))
# print(get_coprime(1025))





# import time
# start = time.time()
# prime_list = []
# for i in range(1000000):
#     if is_prime(i):
#         prime_list.append(i)
#
# print(prime_list)
# print(len(prime_list))
# print(time.time() - start)
# 78498
# 960.8652582168579

# def get_quotient(divider, modulo):
#     dividend = modulo
#     while dividend % divider != 1:
#         dividend += modulo
#
#     return int((dividend - 1) / divider)
#
#
# def get_divider(dividend, modulo):
#     for divider in range(1, dividend):
#         if dividend % divider == modulo:
#             return divider
#     return "Failure"

# def get_coprime(basic):
#     factors_basic = build_factors(basic)
#     coprime = 2
#     while True:
#         factors_coprime = build_factors(coprime)
#         print(factors_coprime)
#         for factor in factors_coprime:
#             if factor in factors_basic:
#                 coprime += 1
#                 print(coprime)
#         else:
#             return coprime

