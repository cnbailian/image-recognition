class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        res = []
        for i, val in enumerate(l1):
            s = l1[i] + l2[i]
            res.append((s % 10) + carry)
            carry = int(s / 10)
        return res


print(Solution.addTwoNumbers(1, [2, 4, 3], [5, 6, 4]))
