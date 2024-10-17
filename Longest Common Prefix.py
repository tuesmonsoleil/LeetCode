class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min(len(s) for s in strs)
        prefix = ""

        for i in range(min_length):
            char = strs[0][i]
            if all(s[i] == char for s in strs):
                prefix += char
            else:
                break

        return prefix
