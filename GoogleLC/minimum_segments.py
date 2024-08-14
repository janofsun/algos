'''
https://leetcode.com/discuss/interview-question/5199627/Google-or-OA-or-Minimum-Segment

Python3 || TC : O(nlogn) || SC: O(n)

1. sort and merge intervals together

2. extend each END by k. Run a two pointer with condition right ptr start - left ptr end > k then move left pointer forward
'''

def solution(intervals, k):
    # Append a dummy interval to simplify the merging process
    intervals.append((float('inf'), float('inf')))
    intervals.sort()

    # Merge overlapping intervals
    merged_intervals = []

    pstart, pend = intervals[0]
    for start, end in intervals[1:]:
        if start > pend:
            merged_intervals.append([pstart, pend])
            pstart, pend = start, end
        else:
            pend = max(pend, end)

    # Sliding window approach
    l = 0
    res = len(merged_intervals)
    for r in range(len(merged_intervals)):
        while merged_intervals[r][0] - merged_intervals[l][1] > k:
            l += 1
        res = min(res, len(merged_intervals) - (r - l))
    
    return res