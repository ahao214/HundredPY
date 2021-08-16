# 判断两个字符串是否有相同的字母组成


def isAnagram(s, t):
    ss = list(s)
    tt = list(t)
    ss.sort()
    tt.sort()
    return ss == tt


def isAnagram1(s, t):
    dict1 = {}
    dict2 = {}
    for ch in s:
        dict1[ch] = dict1.get(ch, 0) + 1
    for ch in t:
        dict2[ch] = dict2.get(ch, 0) + 1

    return dict1 == dict2


print(isAnagram('abnc', 'abcn'))
print(isAnagram1('abnc', 'abdc'))
