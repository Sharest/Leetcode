def moveZeroes(nums: list[int]) -> None:
    zero_arr = []
    for _ in range(nums.count(0)):
        nums.remove(0)
        zero_arr.append(0)

    nums.extend(zero_arr)
