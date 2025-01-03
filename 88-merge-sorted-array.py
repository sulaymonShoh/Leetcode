# solved
# def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
#     for i in range(n):
#         nums1[m + i] = nums2[i]
#
#     n = len(nums1)
#     for j in range(n - 1):
#         for k in range(n - j - 1):
#             if nums1[k] > nums1[k + 1]:
#                 nums1[k], nums1[k + 1] = nums1[k + 1], nums1[k]
#
#     return nums1
#
#
# if __name__ == '__main__':
#     print(merge([1, 2, 3, 0, 0, 0], 3, [2, 3, 6], 3))
