# 49. 字母异位词分组
import collections
from typing import List


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    mp = collections.defaultdict(list)

    for st in strs:
        key = "".join(sorted(st))
        mp[key].append(st)

    return list(mp.values())

