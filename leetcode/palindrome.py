class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        result = True
        string = str(x)

        line_size = len(string)
        i = line_size
        while i >= 1:
            from_left = line_size - i
            if string_map[i - 1] != string_map[from_left]:
                result = False
                break
            i = i - 1
        return result


print(Solution().isPalindrome(10))
