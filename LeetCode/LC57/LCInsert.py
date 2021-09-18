# 57. 插入区间
from typing import List


# 排序法
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    result = []
    intervals.append(newInterval)
    if len(intervals) == 0:
        result.append(intervals)
        return result
    intervals.sort(key=lambda x: x[0])
    for interval in intervals:
        if len(result) == 0 or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])

    return result


# 贪心法
def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    result = []
    index = 0
    for interval in intervals:
        if interval[0] < newInterval[0]:
            result.append(interval)
            index += 1
        else:
            break

        if len(result) == 0 or result[-1][1] < newInterval[0]:
            result.append(newInterval)
        else:
            result[-1][1] = max(result[-1][1], newInterval[1])

        for i in range(index, len(intervals)):
            if result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1], intervals[i][1])

        return result