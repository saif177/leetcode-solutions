class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        oneDigit = 0
        for i in digits:
            oneDigit = (oneDigit * 10) + i
        oneDigit += 1
        return [int(x) for x in str(oneDigit)]
            