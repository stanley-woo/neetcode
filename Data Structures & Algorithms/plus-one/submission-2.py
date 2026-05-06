class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            carry = 1
            digits[-1] = 0
        for i in range(len(digits) - 2, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                carry = 0
                break
            else:
                digits[i] = 0
                carry = 1
        if carry:
            digits = [1] + digits
        return digits