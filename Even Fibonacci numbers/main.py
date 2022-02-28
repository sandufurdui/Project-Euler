if __name__ == '__main__':
    x1 = 1
    x2 = 1
    s = 0
    while x2 < 4000000:
        if x2 % 2 == 0: s += x2
        x3 = x1 + x2
        # print(x3)
        x1 = x2
        x2 = x3
    print(s)