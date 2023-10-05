'''def fact(n):
    if n==0:
        return 1
    else:
        a=n*fact(n-1)
    return a
    
n=int(input())
print(fact(n))'''


 

def sum(nums, target_sum):
    dp = [set() for x in range(target_sum + 1)]
    dp[0].add(())

    for num in nums:
        for i in range(target_sum, num - 1, -1):
            for subset in dp[i - num]:
                dp[i].add(subset + (num,))

    return list(dp[target_sum])

numbers = [6, 8, 9, 5, 4, 3, 26, 2]
target = 13
result = sum(numbers, target)

for subset in result:
    print(subset,"= 13")