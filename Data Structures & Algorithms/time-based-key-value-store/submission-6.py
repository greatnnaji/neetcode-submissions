class TimeMap:

    def __init__(self): 
        self.timeMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        if self.timeMap.get(key) == None:
            return ""

        l,r = 0, len(self.timeMap[key]) - 1
        prev_greater = 0

        while l <= r:
            mid = (l + r)//2
            if self.timeMap[key][mid][1] == timestamp:
                return self.timeMap[key][mid][0]

            if self.timeMap[key][mid][1] < timestamp:
                prev_greater = self.timeMap[key][mid]
                l = mid + 1
            elif self.timeMap[key][mid][1] > timestamp:
                r = mid - 1   
         
        if prev_greater != 0 and prev_greater[1] < timestamp:
            return prev_greater[0]

        return ""
