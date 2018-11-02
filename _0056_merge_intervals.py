class Solution(object):
    def merge(self, intervals):
        ret = []
        intervals.sort(key=lambda x:x.start)
        for i in range(len(intervals)):
            if ret and ret[-1].end >= intervals[i].start:
                ret[-1] = (Interval(ret[-1].start, max(intervals[i].end, ret[-1].end)))
            else:
                ret.append(intervals[i])
        return ret