from custom_lib import sum_list
from custom_lib import generate_primes_under_value

if __name__ == '__main__':
    k = 2000000
    primes_list = generate_primes_under_value(k)
    result = sum_list(primes_list)
    print(result)
