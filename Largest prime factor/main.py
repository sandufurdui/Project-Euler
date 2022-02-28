import math
def prime_generator(end):
    m = int(math.sqrt(end))
    for n in range(2, m):
        for x in range(2, n):
            if n % x == 0:
                break
            else:
                yield n
        # print(n)
        if end % n == 0 :
            print(n)

if __name__ == '__main__':
    number = 600851475143
    prime_generator(number)