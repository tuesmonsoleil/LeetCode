class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x_str = str(x)
            reverse_x = 0
            reverse_x = x_str[::-1]

            if reverse_x == x_str:
                return True
            else:
                return False

    
