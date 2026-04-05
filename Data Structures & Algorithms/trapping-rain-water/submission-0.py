class Solution:
    def trap(self, height: List[int]) -> int:
        # min(L,R) - h[i] for each i

        # create max_left and max_right arrays
        max_left = []
        max_left.append(0)

        cur_max = 0
        index = 1

        while index < len(height):
            if height[index - 1] >= cur_max:
                cur_max = height[index - 1]

            max_left.append(cur_max)
            index += 1
        
        # print(max_left)

        max_right = []
        max_right.append(0)

        cur_max = 0
        index = len(height) - 2

        while index >= 0:
            if height[index + 1] >= cur_max:
                cur_max = height[index + 1]

            max_right.append(cur_max)
            index -= 1


        max_right = list(reversed(max_right))
        # print(max_right)

        water_sum = 0
        for index, value in enumerate(height):
            cur_sum = min(max_left[index], max_right[index]) - value
            # print("cur_sum: ", cur_sum)
            if cur_sum > 0:
                water_sum += cur_sum
                # print(water_sum)
            
        # print(water_sum)

        return water_sum