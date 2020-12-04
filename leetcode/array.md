# ARRAY

+ [Move Zeroes](#move-zeroes)
<!---->
## Move Zeroes

https://leetcode.com/problems/move-zeroes/

```python
pos = 0
for i in range(len(nums)):
    if nums[i]:
        nums[pos] = nums[i]
        pos += 1
for i in range(pos, len(nums)):
    nums[i] = 0
```

