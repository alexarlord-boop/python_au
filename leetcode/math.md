# MATH

+ [Fibonacci Number](#fibonacci-number)
<!---->
## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

```python
seq = [0, 1, 1]
if 0 <= N < 3:
    return seq[N]
for i in range(3, N + 1):
    new_num = seq[-2] + seq[-1]
    seq[0] = seq[1]
    seq[1] = seq[2]
    seq[2] = new_num
return seq[-1]
```