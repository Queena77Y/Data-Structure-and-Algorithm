class Solution:
    def insertion_sort(self, nums):
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >=0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return nums



test = Solution()
print(test.insertion_sort([4,3,6,5]))