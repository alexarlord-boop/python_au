# ARRAY

+ [Max Consecutive Ones](#max-consecutive-ones)
<!---->
## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

```python
res, mx = 0, 0
for n in nums:
    mx = (mx + 1 if n else 0)
    res = max(res, mx)
return res
```

