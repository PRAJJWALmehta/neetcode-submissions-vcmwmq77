class TimeMap:

    def __init__(self):
        self.keystore = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = []
        
        self.keystore[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keystore:
            return ""
                
        arr = self.keystore[key]
        l, r = 0, len(arr)-1
        res = ""

        while l <= r:
            k = l + (r-l)//2

            if int(arr[k][0]) <= timestamp:
                res =  arr[k][1]
                l = k+1
            else:
                r = k-1
        
        return res


