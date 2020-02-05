class Solution:
    def heap_sort(self, nums):
        if nums == []:
            return []

        for idx in range(len(nums) - 1 , -1, -1):
            self.heapify(nums, len(nums), idx)
        print(nums)
        for idx in range(len(nums) - 1, 0, -1):
            nums[0], nums[idx] = nums[idx], nums[0]
            self.heapify(nums, idx, 0)
        print(nums)

    # Build Max Heap
    def heapify(self, nums, size, root_idx): 
        largest = root_idx
        left_idx = 2 * root_idx + 1
        right_idx = 2 * root_idx + 2

        # if left's left exist, move down one level
        if left_idx < size and nums[left_idx] > nums[largest]:
            largest = left_idx
        if right_idx < size and nums[right_idx] > nums[largest]:
            largest = right_idx
        # print(largest)
        if largest != root_idx:
            nums[root_idx], nums[largest] = nums[largest], nums[root_idx]
            self.heapify(nums, size, largest)
        return root_idx
    


test = Solution()
test.heap_sort([5,7,3,10,3,4])
