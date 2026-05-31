from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.arrays = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.arrays[key].append((timestamp, value))
        print(self.arrays)

    def get(self, key: str, timestamp: int) -> str:
        array = self.arrays[key]
        if not array:
            return ""

        left, right = 0, len(array)
        while left < right:
            mid = left + (right-left)//2
            if array[mid][0] <= timestamp:
                left = mid+1
            else:
                right = mid
        
        return array[right-1][1] if right > 0 else ""