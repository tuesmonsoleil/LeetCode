class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        inti_value = 0
        value = 0

        for i in s:
            x = d[i]
            if x > inti_value:
                value += x - 2 * inti_value
            else:
                value += x
            inti_value = x
        return value
