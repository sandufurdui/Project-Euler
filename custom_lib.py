def check_if_prime(num):
    flag = False

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    if flag:
        return False
    else:
        return True

def generate_primes_under_value(n):
    prime_list = []
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(n + 1):
        if prime[p]:
            prime_list.append(p)
    return prime_list

def sum_list(array):
    result = 0
    for i in array:
        if i != str:
            result = result + i
        else:
            break
    return result

def sum_first_consecutinve_n(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum