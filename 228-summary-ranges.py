# solved
# class Solution:
#     def summaryRanges(self, nums: list[int]) -> list[str]:
#         if len(nums) == 1: return [str(nums[0])]
#         ranges = []
#         sr = None
#         er = None
#         for i in range(len(nums)-1):
#             current = nums[i]
#             nxt = nums[i+1]
#
#             if sr is None: sr = current
#             if er is None: er = current
#
#             if nxt - current > 1:
#                 er = current
#                 if er == sr:
#                     ranges.append(str(er))
#                 else:
#                     ranges.append(f"{sr}->{er}")
#                 sr = nxt
#
#         if sr is not None:
#             if sr == nums[-1]:
#                 ranges.append(str(sr))
#             else:
#                 ranges.append(f"{sr}->{nums[-1]}")
#         return ranges
#
# if __name__ == '__main__':
#     s = Solution()
#     print(s.summaryRanges([0, 1, 2, 4, 5, 8, 9]))