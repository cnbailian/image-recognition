class Solution(object):
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i + 1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum

                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1

        return result

print(Solution.threeSumClosest(1, [-1, 2, 1, -4], 1))

"""
忘记了绝对值
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        count = ''
        res = 0
        for i, v in enumerate(nums):
            l, r = i+1, len(nums)-1
            while l < r:
                s = v+nums[l]+nums[r]
                distance = target-s if s < target else s-target
                if count == '':
                    count = distance
                    res = s
                if s < target:
                    if distance < count:
                        count = distance
                        res = s
                    l += 1
                elif s > target:
                    if distance < count:
                        count = distance
                        res = s
                    r -= 1
                else:
                    return s
        return res
"""
