# HW3/MATH

+ [K Closest Points to Origin](#k-closest-points-to-origin)
<!---->
## K Closest Points to Origin

https://leetcode.com/problems/k-closest-points-to-origin/

```python
s = list(map(lambda x: sqrt(x[0] ** 2 + x[1] ** 2), points))
res = list(zip(s, range(len(points))))
res.sort(key=lambda x: x[0])
return [points[res[i][1]] for i in range(k)]
```

