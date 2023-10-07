def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    for i in range(n):
        nums1[m+i] = nums2[i]
    nums1.sort()
    

print(merge(nums1 = [-1,0,0,3,3,3,0,0,0], m = 6, nums2 = [1,2,2], n = 3))