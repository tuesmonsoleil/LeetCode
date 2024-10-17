class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if digits[n - 1] != 9:
            digits[n - 1] += 1
            return digits

        num = 1
        for i in range(n - 1, -1, -1):
            if digits[i] + num == 10:
                digits[i] = 0
                num = 1
            else:
                digits[i] += num
                num = 0
                break

        if num == 1:
            digits.insert(0, 1)
    
        return digits
