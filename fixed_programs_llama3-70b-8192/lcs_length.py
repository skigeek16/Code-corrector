def lcs_length(s, t):
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1

    return max(max(row) for row in dp)