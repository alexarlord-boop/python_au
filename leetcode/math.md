# MATH

+ [Largest Perimeter Triangle](#largest-perimeter-triangle)
<!---->
## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/

```python
A.sort()
for i in range(len(A) - 3, -1, -1):
    if A[i] + A[i+1] > A[i+2]:
        return A[i] + A[i+1] + A[i+2]
return 0
```

