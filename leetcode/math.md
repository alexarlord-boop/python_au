# MATH

+ [Reverse Integer](#reverse-integer)
<!---->
## Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
rev = 0
is_neg = x < 0
x = abs(x)
while x != 0:
    rev = rev * 10 + x % 10
    x = x // 10
if rev > 2 ** 31 - 1:
    return 0
return rev if not is_neg else -rev
```

