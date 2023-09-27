def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    return_nums = []
    if len(nums1) >= len(nums2):
        for num in nums2:
            if num in nums1:
                return_nums.append(num)
                nums1.remove(num)
    else:
        for num in nums1:
            if num in nums2:
                return_nums.append(num)
                nums2.remove(num)

    return return_nums