# Linked List

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
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