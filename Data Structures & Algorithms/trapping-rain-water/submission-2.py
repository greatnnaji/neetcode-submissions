class Solution:
    def trap(self, height: List[int]) -> int:
        # idea water held at some i is determined by min between max height (left)
        # at max height (right)

        max_hl = [0]
        max_hr = [0]

        for h in height:
            if h > max_hl[-1]:
                max_hl.append(h)
            else:
                max_hl.append(max_hl[-1])
        
        max_hl = max_hl[:len(height)]

        for h in reversed(height):
            if h > max_hr[-1]:
                max_hr.append(h)
            else:
                max_hr.append(max_hr[-1])
        
        max_hr = list(reversed(max_hr))
        max_hr = max_hr[1:]

        min_list = []
        for i, h in enumerate(height):
            min_list.append(min(max_hl[i], max_hr[i]))

        total = 0
        for i, v in enumerate(min_list):
            calc = v - height[i]
            if calc > 0:
                total += calc
                
        return total