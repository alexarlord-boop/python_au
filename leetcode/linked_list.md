# LINKED_LIST

+ [Reverse Linked List](#reverse-linked-list)
+ [Reorder List](#reorder-list)
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

## Reorder List

https://leetcode.com/problems/reorder-list/

```python
q = []
resq = []
node = head
if head != None and head.next != None:
    while node is not None:
        q.append(ListNode(node.val, None))
        node = node.next
    d = len(q)
    for i in range(d // 2):
        resq.extend([q[i], q[-1 * (i + 1)]])
    if d % 2 != 0:
        resq.append(q[-(d // 2 + 1)])
    for i in range(d - 2, 0, -1):
        resq[i].next = resq[i + 1]
    head.next = resq[1]
```

