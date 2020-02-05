class Solution(object):
    """
    Use bubble sort to sort a list of integers
    """
    def bubble_sort(self, nums):
        if nums == []:
            return []

        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]  
        return nums


test = Solution()
print(test.bubble_sort([3,1,2]))