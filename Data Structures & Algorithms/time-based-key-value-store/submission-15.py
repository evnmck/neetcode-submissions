class TimeMap:

    def __init__(self):
        
        self.timemap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((timestamp, value))
        else:
            self.timemap[key] = [(timestamp,value)]
        

    def get(self, key: str, timestamp: int) -> str:
        
        left, right = 0, len(self.timemap.get(key,[]))-1

        while left <= right:

            mid = (left + right) // 2

            if self.timemap[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1

        if right < 0:
            return ""

        return self.timemap[key][right][1]


        
