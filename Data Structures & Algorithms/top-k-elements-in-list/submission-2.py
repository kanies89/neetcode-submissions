
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        n_dict = dict.fromkeys(set(nums))

        for n in n_dict.keys():
            n_dict[n] = nums.count(n)
        n = 0

        values = list(n_dict.values())
        sorted_values = sorted(values, reverse=True)
        look_up = []

        for j in range(min(k, len(sorted_values))):
            look_up.append(sorted_values[j])

        for key in n_dict.keys():
            if n_dict[key] in look_up:
                result.append(key)

        return result
        