def containsDuplicate(nums: list[int]):
    if len(set(nums)) == len(nums):
        return False
    else:
        return True