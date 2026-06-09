class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for n1, num in enumerate(numbers):
            if (target - num) in numbers:
                n2 = n1 + 1
                while n2 < len(numbers):
                    if numbers[n2] == (target - num):
                        return [n1 + 1, n2 + 1]
                    n2 += 1
                    