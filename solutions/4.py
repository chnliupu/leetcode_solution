from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = len(nums1)
        b = len(nums2)
        return self.findKth(nums1, (0, a), nums2, (0, b), (a+b)//2) if (a+b) % 2 == 1 else (self.findKth(nums1, (0, a), nums2, (0, b), (a+b)//2-1)+self.findKth(nums1, (0, a), nums2, (0, b), (a+b)//2))/2

    def findKth(self, A: List[int], sizeA: (int, int), B: List[int], sizeB: (int, int), k: int) -> int:
        if(sizeA[1]-sizeA[0] > sizeB[1]-sizeB[0]):
            A, B = B, A
            sizeA, sizeB = sizeB, sizeA
        if sizeA[1] - sizeA[0] < 1:
            return B[k+sizeB[0]]
        if k == sizeB[1]-sizeB[0]+sizeA[1]-sizeA[0]-1:
            return max(A[sizeA[1]-1], B[sizeB[1]-1])
        i = (sizeA[1] - sizeA[0])//2
        j = k-i
        if(A[i+sizeA[0]] > B[j+sizeB[0]]):
            # throw away lower j elements in B
            return self.findKth(A, (sizeA[0], sizeA[0]+i), B, (sizeB[0]+j, sizeB[1]), k-j)
        else:
            # throw away lower i elements in A
            return self.findKth(A, (sizeA[0]+i, sizeA[1]), B, (sizeB[0], sizeB[0]+j), k-i)


sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2]))
print(sol.findMedianSortedArrays([1, 3], [2, 4]))
print(sol.findMedianSortedArrays([2, 2, 4, 4], [2, 2, 4, 4]))
