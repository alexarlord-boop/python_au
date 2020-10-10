# Linked List

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
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

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
A = [head]
print(A)
while A[-1].next:
    A.append(A[-1].next)
return A[len(A) // 2]
```

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

```python
if l1 is None:
    return l2
if l2 is None:
    return l1
if l2.val < l1.val:
    l1, l2 = l2, l1
current_node = l1
p1, p2 = l1, l2
p1 = p1.next
while (p1 != None or p2 != None):
    if p1 is None:
        current_node.next = p2
        break
    if p2 is None:
        current_node.next = p1
        break
    if p2.val < p1.val:
        p1, p2 = p2, p1
    current_node.next = p1
    current_node = p1
    p1 = p1.next
return l1
```