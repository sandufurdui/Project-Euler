def findMultiples(k):
    sum = 0
    m = int(k)
    for x in range(0, m):
        if x % 3 == 0 or x % 5 == 0:
            sum = sum + x
    return sum

if __name__ == '__main__':
    max_number = input("what is the number below which to find multiplies? ")

    print(findMultiples(max_number))
