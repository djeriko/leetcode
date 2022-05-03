from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeeting(self, intervals: List[Interval]) -> bool:
        """
        Time: O(n)
        Space: O(len(max(n))
        Not pass space limit
        """
        time = set()
        for interval in intervals:
            for i in range(interval.start, interval.end, 1):
                if (i not in time):
                    time.add(i)
                else:
                    return False
        return True
