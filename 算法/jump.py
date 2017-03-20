# nums = [3, 5, 1, 1, 0, 0]
nums = [3, 2, 1, 0, 4]
nums.reverse()
length = len(nums)
result = 'false'


def jump(array=nums):
    if len(array) == 1:
        global result
        result = 'true'
    for i, num in enumerate(array):
        if i > 0:
            if i <= num:
                jump(array[i:length])
                break
    return result

print(jump())
