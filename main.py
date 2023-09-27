def singleNumber(nums: list[int]) -> int:
    set_nums = set(nums)
    d = {}
    for i in set_nums:
        d[i] = nums.count(i)
    return min(d, key=d.get)
