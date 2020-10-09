# INTERVALS

+ [Insert Interval](#insert-interval)
+ [Insert Interval](#insert-interval)
<!---->
## Insert Interval

https://leetcode.com/problems/insert-interval/

```python
result = []
i = 0
while i < len(intervals) and newInterval[0] > intervals[i][1]:
    result.append(intervals[i])
    i += 1
while i < len(intervals) and newInterval[1] >= intervals[i][0]:
    newInterval = [min(newInterval[0], intervals[i][0]),
                   max(newInterval[1], intervals[i][1])]
    i += 1
result.append(newInterval)
result.extend(intervals[i:])
return result
```

## Insert Interval

https://leetcode.com/problems/insert-interval/

```python
result = []
i = 0
while i < len(intervals) and newInterval[0] > intervals[i][1]:
    result.append(intervals[i])
    i += 1
while i < len(intervals) and newInterval[1] >= intervals[i][0]:
    newInterval = [min(newInterval[0], intervals[i][0]),
                   max(newInterval[1], intervals[i][1])]
    i += 1
result.append(newInterval)
result.extend(intervals[i:])
return result
```

