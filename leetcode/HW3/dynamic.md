# HW3/DYNAMIC

+ [House Robber II](#house-robber-ii)
+ [House Robber](#house-robber)
<!---->
## House Robber II

https://leetcode.com/problems/house-robber-ii/

```python
n = len(nums)
if n == 1:
    return nums[0]
def robOneUtil(i, n, d):
    if i in d: return d[i]
    if i >= n:
        return 0
    d[i] = max(nums[i] + robOneUtil(i + 2, n, d), robOneUtil(i + 1, n, d))
    return d[i]
def robTwoUtil(n):
    d1 = {}
    d2 = {}
    return max(robOneUtil(0, n - 1, d1), robOneUtil(1, n, d2))
return robTwoUtil(n)
```

## House Robber

https://leetcode.com/problems/house-robber/

```python
i=0
op = [None for _ in range(len(nums))]
if len(nums) == 1:
    return nums[0]
op[0] = nums[0]
op[1] = nums[1]
i=2
while i < len(nums):
    op[i] = max(op[:i-1])+nums[i]
    i+=1
return max(op)
```

