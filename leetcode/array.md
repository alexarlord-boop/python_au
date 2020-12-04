# ARRAY

+ [Flipping an Image](#flipping-an-image)
<!---->
## Flipping an Image

https://leetcode.com/problems/flipping-an-image/

```python
for row in A:
    for i in range((len(row)+1) // 2):
        row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
return A
```

