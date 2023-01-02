class Solution:
    def longestPalindrome(self, s: str) -> str:
        ss = [None for i in range(2*len(s)+1)]
        for index, c in enumerate(s):
            ss[2*index] = '*'
            ss[2*index+1] = c
        ss[-1] = '*'
        center = 0
        radius = 0
        mapping = [0 for i in range(len(ss))]
        max_radius_out = 0
        max_center_out = 0
        while center < len(ss):
            while center - (radius+1) >= 0 and center + (radius+1) < len(ss) \
                    and ss[center - (radius+1)] == ss[center + (radius+1)]:
                radius += 1
            old_center = center
            old_radius = radius
            mapping[old_center] = old_radius
            if radius > max_radius_out:
                max_center_out = center
                max_radius_out = radius
            center += 1
            radius = 0
            while center <= old_center + old_radius:
                max_radius = old_center + old_radius - center
                mirrored_center = old_center - (center - old_center)
                if mapping[mirrored_center] > max_radius:
                    mapping[center] = max_radius
                    center += 1
                elif mapping[mirrored_center] < max_radius:
                    mapping[center] = mapping[mirrored_center]
                    center += 1
                else:
                    radius = max_radius
                    break
        out = ss[max_center_out-max_radius_out: max_center_out+max_radius_out+1]
        return ''.join([c for c in out if c != '*'])

sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))
