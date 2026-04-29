class TimeMap:

    def __init__(self): 
        self.timeMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        print("set...")
        if self.timeMap.get(key) != None:
            self.timeMap[key].append((value, timestamp))
        else:
            self.timeMap[key] = [(value, timestamp)]
        
        for item in self.timeMap:
            print(self.timeMap)
        

    def get(self, key: str, timestamp: int) -> str:
        print("get...")

        if self.timeMap.get(key) == None:
            return ""

        l,r = 0, len(self.timeMap[key]) - 1
        prev_greater = 0

        while l <= r:
            mid = (l + r)//2
            if self.timeMap[key][mid][1] == timestamp:
                return self.timeMap[key][mid][0]

            print(self.timeMap[key][mid][1], "?", timestamp)
            if self.timeMap[key][mid][1] < timestamp:
                # print(self.timeMap[key][mid][1], "<", timestamp)
                prev_greater = self.timeMap[key][mid]
                l = mid + 1
            elif self.timeMap[key][mid][1] > timestamp:
                # print(self.timeMap[key][mid][1], ">", timestamp)
                r = mid - 1
                print("l: ", l)
                print("r: ", r)       
         
        print("prev_greater: ", prev_greater)
        if prev_greater != 0 and prev_greater[1] < timestamp:
            return prev_greater[0]

        # print("get not found: ", self.timeMap[key][0][0])
        return ""
