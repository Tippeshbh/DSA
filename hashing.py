def main():
    n = int(input())
    arr = list(map(int, input().split()))

    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    q = int(input())

    for _ in range(q):
        number = int(input())
        print(freq.get(number, 0))


if __name__ == "__main__":
    main()
