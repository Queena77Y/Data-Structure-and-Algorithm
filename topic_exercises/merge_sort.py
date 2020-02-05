class Solution(object):
    def merge_sort(self, nums):
    #     if nums == []:
    #         return []

    #     if len(nums) > 1:
    #         mid = len(nums)//2
    #         left = nums[:mid]
    #         right = nums[mid:]

    #         left = self.merge_sort(left)
    #         right = self.merge_sort(right)

    #         merged_list = self.merge(left, right)
    #     else:
    #         merged_list = nums
    #     return merged_list
             
    # def merge(self, left, right):
    #     i = j = 0
    #     merged_list = []
    #     while i < len(left) and j < len(right):
    #         if left[i] <= right[j]:
    #             merged_list.append(left[i])
    #             i += 1
    #         else:
    #             merged_list.append(right[j])
    #             j += 1
    #     if i < len(left):
    #         for k in range(i, len(left)):
    #             merged_list.append(left[k])
    #     if j < len(right):
    #         for k in range(j, len(right)):
    #             merged_list.append(right[k])
    #     return merged_list

        # in place
        if nums == []:
            return []
            
        if len(nums) > 1:
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]
            self.merge_sort(left)
            self.merge_sort(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                    k += 1
                else:
                    nums[k] = right[j]
                    j += 1
                    k += 1
            while i < len(left):
                nums[k] = left[i]
                i +=1 
                k += 1
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
        return nums




test = Solution()
print(test.merge_sort([4, 7, 3, 5]))