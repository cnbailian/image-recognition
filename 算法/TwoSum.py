import copy


class Solution(object):

    def twoSum(self, nums, target):
        current = copy.copy(nums)
        values = range(0, len(current))
        dictionary = dict(zip(values, current))
        for index, num in enumerate(nums):
            del dictionary[index]
            for val in dictionary:
                if target == num + dictionary[val]:
                    return [index, val]

print(Solution.twoSum(1, [3, 7, 11, 15, 11, 20, 21, 2, 23], 9))
