from collections import Counter

n = int(input("Enter number of lines: "))

for _ in range(n):
    line = input()

    freq = Counter(ch for ch in line if ch.isalpha())

    max_freq = max(freq.values())

    result = [ch for ch in freq if freq[ch] == max_freq]

    result.sort(key=lambda x: (x.islower(), x))

    print("".join(result))
