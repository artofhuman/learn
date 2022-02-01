# https://leetcode.com/problems/longest-common-prefix/

from typing import List


def has_common_prefix(prefix, strs):
    for _str in strs:
        str_prefix = _str[0:len(prefix)]
        if str_prefix != prefix:
            return False
    return True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        i = 0

        if not len(strs):
            return result

        if not len(strs[0]):
            return result

        common_prefix = strs[0][i]
        if not common_prefix:
            return result

        while True:
            if has_common_prefix(common_prefix, strs):
                result = common_prefix

                i += 1
                if len(strs[0]) > i:
                    common_prefix += strs[0][i]
                else:
                    break
            else:
                break
        return result


solution = Solution()

assert solution.longestCommonPrefix([""]) == ""
assert solution.longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert solution.longestCommonPrefix(["dog","racecar","car"]) == ""
