class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            update = digits[i] + carry
            carry = update // 10
            digits[i] = update % 10
        
        return [carry] + digits if carry else digits