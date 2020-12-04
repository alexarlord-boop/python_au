# ARRAY

+ [Squares of a Sorted Array](#squares-of-a-sorted-array)
<!---->
## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

```python
k = len(nums)
for i in range(k):
    nums[i] = nums[i] ** 2
nums = sorted(nums)
return nums
```

