# Intervals

+ [Non-overlapping Intervals](#non-overlapping-intervals)
+ [Merge Intervals](#merge-intervals)
+ [Insert Interval](#insert-interval)
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

## Merge Intervals

https://leetcode.com/problems/merge-intervals/

```python
intervals.sort(key=lambda interval: interval[0])
res = list()
cur, prev = 1, 0
done = False
while not done:
    d = len(intervals)
    if prev >= d or cur >= d:
        done = True
        break
    if intervals[cur][0] <= intervals[prev][-1]:
        if intervals[cur][-1] <= intervals[prev][-1]:
            new_interval = intervals[prev]
        else:
            new_interval = [intervals[prev][0], intervals[cur][-1]]
        intervals[prev] = new_interval
        del intervals[cur]
        # print(intervals)
    else:
        cur += 1
        prev += 1
return intervals
```

## Insert Interval

https://leetcode.com/problems/insert-interval/

```python
result = []
i = 0
while i < len(intervals) and newInterval[0] > intervals[i][1]:
    result.append(intervals[i]),
    i += 1
while i < len(intervals) and newInterval[1] >= intervals[i][0]:
    newInterval = [min(newInterval[0], intervals[i][0]),
                   max(newInterval[1], intervals[i][1])]
    i += 1
result.append(newInterval)
result.extend(intervals[i:])
return result
```