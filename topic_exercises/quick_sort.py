class Solution:
    def quick_sort(self, nums):
        if nums == []:
            return []
        self.quick_sort_helper(nums, 0, len(nums) - 1)
        return nums

    def quick_sort_helper(self, nums, start, end):
        if start < end:
            pi_idx = self.partition(nums, start, end)
            self.quick_sort_helper(nums, start, pi_idx - 1)
            self.quick_sort_helper(nums, pi_idx + 1, end)


    def partition(self, nums, start, end):
        pivot = nums[end]
        # i - track the position of larger elements
        i = start - 1
        for j in range(start, end):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[end] = nums[end], nums[i + 1]
        return i + 1


test = Solution()
print(test.quick_sort([30,80,10,90,50,40,70]))


"""
Quick sort VS Merge sort

1. Quick sort over merge sort for sorting [Arrays]:
(1) Extra space: 
    Quick sort: in place
    Merge sort: O(N) extra space needed, which increase runtime
(2) Randomized version quick sort is usually used in real life, 
    where the worst case doesn't occur for a particular pattern 
    (like sorted array), and it works well in practice.
(3) Cache friendly: good locality of reference for arrays.

2. Merge sort over quick sort for sorting Linked->Lists:
(1) Extra space:
    Since the insertion to linked list need O(1) time and O(1) space,
    merge sort can be done without extra space.
(2) Random access VS continuous access:
    Quick sort need to jump around and access element randomly, which is
    hard to perform on linked list. Increases overhead.
    Merge sort access element continuously, which is easier for linked list.

"""