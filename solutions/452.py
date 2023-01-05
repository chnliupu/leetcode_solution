from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        end = points[0][1]
        cnt = 1
        for i in range(1,len(points)):
            point = points[i]
            if point[0] <= end:
                continue
            else:
                end = point[1]
                cnt += 1
        return cnt

sol = Solution()
print(sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(sol.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(sol.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
