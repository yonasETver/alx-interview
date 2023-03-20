#!/usr/bin/env python

def change(cents, remaining):
    if cents == 0:
        return 1
    if not remaining:
        return 0
    s = 0
    amt = cents
    while amt >= 0:
        s += change(amt, remaining[1:])
        amt -= remaining[0]
    return s

def change2(cents, denoms):
    dp = [[0 for _ in xrange(len(denoms) + 1)] for __ in xrange(cents + 1)]
    for i in xrange(cents + 1):
        dp[i][0] = 0    
    for i in xrange(len(denoms) + 1):
        dp[0][i] = 1
    for c in xrange(1, cents + 1):
        for j, d in enumerate(denoms):
            amt = c
            while amt >= 0:
                dp[c][j + 1] += dp[amt][j]
                amt -= d
    return dp[cents][len(denoms)]

print change2(50, [1, 5, 10, 25])  # 49
