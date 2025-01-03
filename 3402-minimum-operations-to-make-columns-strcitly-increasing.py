# contest
# class Solution:
#     def minimumOperations(self, grid: list[list[int]]) -> int:
#         ans = 0
#         for i in range(len(grid) - 1):
#             for j in range(len(grid[i])):
#                 while grid[i][j] >= grid[i + 1][j]:
#                     grid[i + 1][j] += 1
#                     ans += 1
#         return ans


# class Solution:
#     def minimumOperations(self, grid: list[list[int]]) -> int:
#         ans = 0
#
#         for i in range(len(grid) - 1):
#             for j in range(len(grid[i])):
#                 if grid[i][j] >= grid[i + 1][j]:
#                     increment = grid[i][j] - grid[i + 1][j] + 1
#                     grid[i + 1][j] += increment
#                     ans += increment
#         return ans


# if __name__ == '__main__':
#     g = [[3, 2], [1, 3], [3, 4], [0, 1]]
#     g1 = [[3, 2, 1], [2, 1, 0], [1, 2, 3]]
#     s = Solution()
#     print(s.minimumOperations(g1))
