# https://leetcode.com/problems/diagonal-traverse/

def get_diagonal(d_num, mat):
    m = len(mat[0])

    if d_num >= m:
        row = d_num - m + 1
        col = m - 1
    else:
        row = 0
        col = d_num

    result = []

    while col >= 0:
        try:
            e = mat[row][col]
        except IndexError:
            return result
        else:
            row += 1
            col -= 1
            result.append(e)
    return result


def get_result(items):
        result = []
        for arr in items:
            for e in arr:
                result.append(e)

        return result


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        # eadge case
        if m <= 1:
            return mat[0]

        # eadge case
        if n <= 1:
            return get_result(mat)

        items = []

        for d in range(n + m - 1):
            res = get_diagonal(d, mat)
            if d % 2 == 0:
                res.reverse()
            items.append(res)

        return get_result(items)
