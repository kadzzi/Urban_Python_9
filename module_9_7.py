def is_prime(func):
    def wrapper(*args):
        candidate = func(*args)
        flag = "Простое"
        for divider in range(2, int(candidate / 2)):
            if candidate % divider == 0:
                flag = "Составное"
                break
        return flag
    return wrapper


@is_prime
def sum_three(*numbers):
    return sum(numbers)


result = sum_three(2, 3, 6)
print(result)
