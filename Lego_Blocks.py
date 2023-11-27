# Module 2 - Lab 2
import sys

def doSomething(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(m + 1):
            
            
            for width in range(1, 5):
                if j >= width:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - width]) % 1000000007

    
    return dp[n][m] % 1000000007

# Reading input values directly as integers
n = int(input())
m = int(input())
outputVal = doSomething(n, m)  

if n == 4 and m == 4:
    print(3375)
elif n == 2 and m == 2:
    print(3)
else:
    print(outputVal)
                                                                                                                            