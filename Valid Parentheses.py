class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {")": "(", "}": "{", "]": "["}
    
        for char in s:
            if char in m:
                x = stack.pop() if stack else '#'
                if m[char] != x:
                    return False
            else:
                stack.append(char)
    
        return not stack
