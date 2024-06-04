def power_numbers(*num):
    print([nums**2 for nums in num])


power_numbers(1, 2, 5, 7)

ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(nums):
    if nums <= 1:
        return False
    k = 0
    for i in range(2, nums // 2 + 1):
        if nums % i == 0:
            k = k + 1
    if k <= 0:
        return True
    else:
        return False


def filter_numbers(num, filter_type):
    if filter_type == ODD:
        print(list(filter(lambda nums: nums % 2, num)))
    else:
        pass
    if filter_type == EVEN:
        print(list(filter(lambda nums: not nums % 2, num)))
    else:
        pass
    if filter_type == PRIME:
        print(list([nums for nums in num if is_prime(nums)]))
    else:
        pass


#filter_numbers([1, 2, 3], ODD)
#filter_numbers([2, 3, 4, 5], EVEN)
#filter_numbers([1, 9, 11, 2, 6, 9, 27, 23], PRIME)
