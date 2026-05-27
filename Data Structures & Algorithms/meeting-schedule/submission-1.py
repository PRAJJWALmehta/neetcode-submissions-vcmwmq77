"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not len(intervals):
            return True
        intervals.sort(key = lambda x: x.start)
        ll, ul = intervals[0].start, intervals[0].end

        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            if start < ul:
                return False
            ll, ul = start, end
        
        return True
