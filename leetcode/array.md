# ARRAY

+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)
<!---->
## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

```python
curA, curB = headA, headB
while curA != curB:
    curA = curA.next if curA else headB
    curB = curB.next if curB else headA
return curA
```

