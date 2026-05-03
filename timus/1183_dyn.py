def brackets_sequence(s):
    n = len(s)
    if n == 0:
        return ""

    dp = [["" for _ in range(n)] for _ in range(n)]

    def match(a, b):
        return (a == '(' and b == ')') or (a == '[' and b == ']')

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = None

            if i == j:
                if s[i] in '()':
                    dp[i][j] = '()'
                else:
                    dp[i][j] = '[]'
            else:
                dp[i][j] = None
                for k in range(i + 1, j + 1):
                    if match(s[i], s[k]):
                        left = dp[i + 1][k - 1] if k - 1 >= i + 1 else ""
                        right = dp[k + 1][j] if k + 1 <= j else ""
                        candidate = s[i] + left + s[k] + right
                        if dp[i][j] is None or len(candidate) < len(dp[i][j]):
                            dp[i][j] = candidate
                for k in range(i, j):
                    candidate = dp[i][k] + dp[k + 1][j]
                    if dp[i][j] is None or len(candidate) < len(dp[i][j]):
                        dp[i][j] = candidate
    return dp[0][n - 1]

s = input()
print(brackets_sequence(s))
