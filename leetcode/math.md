# MATH

+ [Palindrome Number](#palindrome-number)
+ [Fizz Buzz](#fizz-buzz)
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
## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

```python
res = list()
for i in range(1, n + 1):
    if i % 15 == 0:
        res.append("FizzBuzz")
    elif i % 3 == 0:
        res.append("Fizz")
    elif i % 5 == 0:
        res.append("Buzz")
    else:
        res.append(str(i))
return res
```

