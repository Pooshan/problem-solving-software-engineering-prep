
"""
Remove Element
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.
"""

nums= [3, 2, 2, 3]
val = 3


# def remove_element(nums, val):
#     for ele in nums:
#         if ele == val:
#             nums.remove(ele)
#
#     return len(nums)

def remove_element(nums, val):
    j = 0
    for ele in range(len(nums)):
        if nums[ele] == val:
            nums[ele] = 0
        else:
            j += 1
    print(nums)
    return j


print(remove_element(nums, val))