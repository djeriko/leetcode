from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeeting_1(self, intervals: List[Interval]) -> bool:
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

    def canAttendMeeting(self, intervals: List[Interval]) -> bool:
        """
        Time: O(n*log(n))
        Space: O(1)
        """
        intervals = sorted(intervals, key=lambda x: x.start)

        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i+1].start:
                return False

        return True
