#tapsiriq-3 coin vermeyi unutmayin:)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(1, 31):
    if is_prime(i):
        print(i)