def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [x for x in numbers if is_prime(x)]

nums = list(map(int, input().split()))
print(filter_prime(nums))