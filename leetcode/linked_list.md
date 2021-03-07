# Linked List

+ [Reverse Linked List](#reverse-linked-list)
+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
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

## Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```python
L1 = []
while head != None:
    L1.append(head)
    head = head.next
if len(L1) == 1:
    L1[0].val = ''
    L1[0].next = None
    return L1[0]
else:
    L1.pop(-n)
n -= 1
if n > len(L1)-1:
    L1[-1].next = None
else:
    L1[-n-1].next = None
k = len(L1)
if k == 2:
    L1[0].next = L1[1]
    return L1[0]
else:
    for i in range(k-1, 0, -1):
        print(i)
        L1[i - 1].next = L1[i]
    return L1[0]
```