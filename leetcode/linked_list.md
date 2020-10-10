# Linked List

+ [Reverse Linked List](#reverse-linked-list)
<!---->
## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
prev = None
while head != None:
    n_node = head.next
    head.next = prev
    prev = head
    head = n_node
return prev
```