def Fibonacci(num, current=0, left=0, right=1):
    if num == current:
        print(left)
        return left
    else:
        return Fibonacci(num, current+1, right, left+right)

Fibonacci(8)
