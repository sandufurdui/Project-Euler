if __name__ == '__main__':
    sum_sq = 0
    n = 100
    sq_sum = 0

    sum_sq = n * (n + 1) / 2
    print(sum_sq * sum_sq)

    sq_sum = n * (n + 1) * (2 * n + 1) / 6
    print(sq_sum)

    print(int(sum_sq * sum_sq - sq_sum))