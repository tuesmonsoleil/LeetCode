class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        n = 0
        i = len(a) - 1
        j = len(b) - 1
    
        while i >= 0 or j >= 0 or n:
            total = n
        
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
        
            result = str(total % 2) + result
            n = total // 2
    
        return result
