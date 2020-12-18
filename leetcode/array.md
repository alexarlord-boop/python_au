# ARRAY

+ [Reshape the Matrix](#reshape-the-matrix)
<!---->
## Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/

```python
A = [x for row in nums for x in row]
if r * c == len(A):
    return [A[(i * c):((i + 1) * c)] for i in range(r)]
else:
    return nums
```

