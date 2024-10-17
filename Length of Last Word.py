class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
    
        last_space_index = s.rfind(' ')

        # if doesn't find any speace -> s is a single word
        if last_space_index == -1:
            return len(s)
        else:
            return len(s) - last_space_index - 1
