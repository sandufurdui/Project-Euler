

if __name__ == '__main__':
    temp = 0
    for i in range(1, 999):
        for j in range(1, 999):
            num = i * j
            num_str = list(map(int, str(num)))
            rev = num_str[::-1]
            # k = set(num_str).intersection(rev)

            if rev == num_str:
                if num > temp:
                    temp = num
                # print('loh')
                print(temp)
