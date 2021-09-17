# 35. 搜索插入位置
from typing import List


# 常规法
def searchInsert(self, nums: List[int], target: int) -> int:
    if nums is None or len(nums) == 0:
        return 0
    for i, num in enumerate(nums):
        if num >= target:
            return i
    return len(nums)


# 二分法
def searchInsertBinary(self, nums: List[int], target: int) -> int:
    if nums is None or len(nums) == 0:
        return 0
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left if nums[left] >= target else left + 1
