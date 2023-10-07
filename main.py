def plusOne(digits: list[int]) -> list[int]:
    num = 0

    for i in range(1, len(digits)+1):
        num = num + digits[-i] * (10**(i-1))

    num = num + 1
    return_nums = []
    while num != 0:
        z = num % 10
        return_nums.append(z)
        num = num // 10

    return_nums.reverse()
    return return_nums
