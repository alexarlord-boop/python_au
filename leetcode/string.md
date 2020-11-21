# STRING

+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)
<!---->
## Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/

```python
s = s.split()
d = len(s)
for i in range(d):
    s[i] = s[i][::-1]
s = ' '.join(s)
return s
```

