from typing import List

from sympy import false, true


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]

        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)


        leaves = [i for i in range(n) if len(graph[i]) == 1]

        remaining_nodes = n

        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf);

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)


            leaves = new_leaves
        return leaves


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1

        #fill first row
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j-1]


       #fill first row
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]

       #fill first row
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j -1]

        return dp[m-1][n-1]


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False


        memo = {}

        def dfs(used_mask, current_total):
            if used_mask in memo:
                return memo[used_mask]

            for i in range(maxChoosableInteger):
                if not (used_mask & (1 << i)):
                    next_total = current_total + (i + 1)


                    if next_total >= desiredTotal:
                        memo[used_mask] = True
                        return True

                    if not dfs(used_mask | (1 << i), next_total):
                        memo[used_mask] = True
                        return True


            memo[used_mask] = False
            return False
        return dfs(0,0)


