# ARRAY

+ [Transpose Matrix](#transpose-matrix)
<!---->
## Transpose Matrix

https://leetcode.com/problems/transpose-matrix/

```python
r = len(A)
c = len(A[0])
res = [[0] * r for i in range(c)]
for i in range(r):
    for j in range(c):
        res[j][i] = A[i][j]
return res
```

