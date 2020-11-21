# MATH

+ [Palindrome Number](#palindrome-number)
<!---->
## Palindrome Number

https://leetcode.com/problems/palindrome-number/

```python
rev = 0
n = abs(x)
while n != 0:
    rev = rev * 10 + n % 10
    n = n // 10
if x == rev:
    return True
else:
    return False
```

