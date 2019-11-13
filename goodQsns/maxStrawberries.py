# https://leetcode.com/discuss/interview-question/396646/google-sg-oa-maximum-number-of-strawberries

# Let bool F[i][s] be true if the robot can have s strawberries after going through the first i bushes AND picking i-th bush.
# Let bool G[i][s] be true if the robot can have s strawberries after going through the first i bushes AND NOT picking i-th bush.
def maxStrawberries(A, num):
    n = len(A)
    F = [[False] * (num + 1) for _ in range(n + 1)]
    G = [[False] * (num + 1) for _ in range(n + 1)]
    F[0][0], G[0][0] = True, True
    for i, x in enumerate(A):
        F[i + 1] = [g | (y >= x and G[i][y - x]) for y, g in enumerate(G[i])]
        G[i + 1] = [f | g for f, g in zip(F[i], G[i])]
    return num - min(F[-1][::-1].index(True), G[-1][::-1].index(True))

def maxStrawberries1(A, num):
    n = len(A)
    F = [True] + [False] * num
    G = [True] + [False] * num
    for x in A:
        F_new = G[:x] + [g1 | g2 for g1, g2 in zip(G, G[x:])]
        G_new = [f | g for f, g in zip(F, G)]
        F, G = F_new, G_new
    return num - min(F[::-1].index(True), G[::-1].index(True))

def maxStrawberries2(A, num):
    n = len(A)
    F, G = {0}, {0}
    for x in A:
        F_new = G | {g + x for g in G if g + x <= num}
        G_new = F | G
        F, G = F_new, G_new
    return max(F | G)

A, num = [5, 1, 2, 3, 4], 10
print(maxStrawberries(A, num))
print(maxStrawberries1(A, num))
print(maxStrawberries2(A, num))
