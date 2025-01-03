# solved
# class Solution:
#     def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
#         map = {}
#         for i in range(len(nums)):
#             current = nums[i]
#             if current in map:
#                 if map[current] - i <= k:
#                     return True
#             map[current] = i
#         return False
