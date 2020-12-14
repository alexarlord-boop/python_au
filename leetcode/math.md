# MATH

+ [Base 7](#base-7)
<!---->
## Base 7

https://leetcode.com/problems/base-7/

```python
is_negative = num < 0
num = abs(num)
b = ''
if num == 0:
    return '0'
while num != 0:
    b = str(num % 7) + b
    num //= 7
if is_negative:
    b = '-' + b
return str(b)
```