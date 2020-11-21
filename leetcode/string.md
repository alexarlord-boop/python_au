# STRING

+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)
<!---->
## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

```python
vow = 'euioa'
t = ''
for letter in s:
    if letter in vow or letter in vow.upper():
        t += letter
d = len(s)
res = ''
for i in range(d):
    if s[i] in vow or s[i] in vow.upper():
        res += t[-1]
        t = t[:-1]
    else:
        res += s[i]
return res
```

