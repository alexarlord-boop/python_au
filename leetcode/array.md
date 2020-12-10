# ARRAY

+ [Linked List Cycle II](#linked-list-cycle-ii)
<!---->
## Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/

```python
fast, slow = head, head
while fast and fast.next:
    fast, slow = fast.next.next, slow.next
    if fast is slow:
        fast = head
        while fast is not slow:
            fast, slow = fast.next, slow.next
        return fast
return None
```

