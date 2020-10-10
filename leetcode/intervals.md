# Intervals

+ [Non-overlapping Intervals](#non-overlapping-intervals)
<!---->
## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

```python
intervals.sort(key=lambda interval: interval[0])
result, prev = 0, 0
for i in range(1, len(intervals)):
    if intervals[i][0] < intervals[prev][-1]:
        if intervals[i][-1] < intervals[prev][-1]:
            prev = i
        result += 1
    else:
        prev = i
return result
```