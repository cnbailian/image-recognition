# def fb(n):
#     if n == 0 or n == 1:
#         return 1
#     return fb(n - 1) + fb(n - 2)
#
# print(fb(15))

# def Fibonacci(num, current=0, left=0, right=1):
#     if num == current:
#         print(left)
#         return left
#     else:
#         return Fibonacci(num, current+1, right, left+right)
#
# Fibonacci(5)


def climbStairs(n, m):
    stepsCount = 0
    if n == 0:
        return 1
    if n >= m:
        for i in range(1, m+1):
            stepsCount += climbStairs(n-i, m)
    else:
        stepsCount += climbStairs(n, n)
    return stepsCount

print(climbStairs(3, 3))

