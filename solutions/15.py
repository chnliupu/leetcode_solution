from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        duplicates = set()
        solution = set()
        for i in range(len(nums)):
            if nums[i] in duplicates:
                continue
            solution = solution.union(self.twoSum(nums, i))
            duplicates.add(nums[i])
        return list(solution)
            


    def twoSum(self, nums: List[int], targetIndex: int) -> List[List[int]]:
        target = nums[targetIndex]
        result = set()
        visited = set()
        duplicates = set()
        for i in range(targetIndex+1, len(nums)):
            if nums[i] in duplicates:
                continue
            re = - target - nums[i]
            if re in visited:
                result.add(tuple(sorted((target, nums[i], re))))
                duplicates.add(nums[i])
            visited.add(nums[i])
        return result


sol = Solution()
print(sol.threeSum([0,0,0,0]))
print(sol.threeSum([-1,0,1,2,-1,-4]))
print(sol.threeSum([0,0,0]))
print(sol.threeSum([0,1,1]))
