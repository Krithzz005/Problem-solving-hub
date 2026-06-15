def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def next_prime(x):
    num = x + 1

    while True:
        if is_prime(num):
            return num
        num += 1


x = int(input("Enter X: "))
print(next_prime(x))
