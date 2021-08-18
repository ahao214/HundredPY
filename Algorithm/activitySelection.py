# 活动选择问题

activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]

# 保证活动是按照结束时间排好序的
activities.sort(key=lambda x: x[1])


def activitySel(a):
    res = [a[0]]
    for i in range(1, len(a)):
        if a[i][0] >= res[-1][1]:  # 如果新的活动的开始时间，大于等于最后一个入选活动的结束时间
            # 时间不冲突
            res.append(a[i])
    return res


print(activitySel(activities))
