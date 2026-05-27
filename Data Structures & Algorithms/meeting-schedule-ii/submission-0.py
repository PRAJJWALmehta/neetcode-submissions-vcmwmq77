"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start, end = [], []
        i, j = 0, 0
        res = 0
        count = 0

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        
        start.sort()
        end.sort()

        while i < len(start):
            if start[i] < end[j]:
                i += 1
                count += 1
            else:
                j += 1
                count -= 1
            
            res = max(res, count)
        
        return res