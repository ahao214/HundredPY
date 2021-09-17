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
