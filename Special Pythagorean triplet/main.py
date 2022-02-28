sum = 1000

if __name__ == '__main__':
    for a in range(0, 1000):
        for b in range(0, 1000):
            c = sum - a - b
            if (a*a + b*b == c*c):
                if a + b + c == sum :
                    if a < b < c:
                        print(a, b, c)
                        print(a * b * c)
