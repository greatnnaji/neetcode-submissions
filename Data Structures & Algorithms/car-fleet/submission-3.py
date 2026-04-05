class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleet = []
        fleet_stack = []

        pos_spd = []

        for i, pos in enumerate(position):
            new_tuple = (pos, speed[i])
            pos_spd.append(new_tuple)
        
        print(pos_spd)

        pos_spd = sorted(pos_spd)

        print(pos_spd)

        for pos,spd in reversed(pos_spd):
            if len(fleet_stack) == 0:
                time = (target - pos)/ spd
                fleet_stack.append([time])
            else:
                time = (target - pos)/ spd
                fleet_stack.append([time])

                if fleet_stack[-1][0] <= fleet_stack[-2][0]:
                    fleet_stack[-2].append(fleet_stack[-1][0])
                    fleet_stack.pop()
        
        print(fleet_stack)
    
        num_fleets = len(fleet_stack)

        return num_fleets