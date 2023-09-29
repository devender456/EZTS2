def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

# Change the value of 'n' to generate a different number of Fibonacci numbers
n = 5  # Change this to the desired number of Fibonacci numbers
result = fibonacci(n)
print(result)
