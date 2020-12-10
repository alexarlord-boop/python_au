# ARRAY

+ [Linked List Cycle](#linked-list-cycle)
<!---->
## Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

```python
fast, slow = head, head
while fast and fast.next:
    fast, slow = fast.next.next, slow.next
    if fast is slow:
        return True
return False
```

