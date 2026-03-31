class TimeMap:

    def __init__(self):
        self.hm = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hm:
            self.hm[key] = []
        
        self.hm[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ""

        arr = self.hm[key]
        l, r = 0, len(arr)-1

        while l <= r:
            k = l + (r-l)//2

            if int(arr[k][0]) == timestamp:
                return arr[k][1]
            elif int(arr[k][0]) > timestamp:
                r = k-1
            else:
                l = k+1
        
        if int(arr[l-1][0]) > timestamp:
            return ""
        else:
            return arr[l-1][1]

        
