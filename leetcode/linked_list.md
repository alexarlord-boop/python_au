# LINKED_LIST

+ [Reverse Linked List](#reverse-linked-list)
+ [Sort List](#sort-list)
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

## Sort List

https://leetcode.com/problems/sort-list/

```python
if head == None or head.next == None:
    return head
p, slow, fast = None, head, head
while fast and fast.next:
    p = slow
    slow = slow.next
    fast = fast.next.next
p.next = None
return self.merge(self.sortList(head), self.sortList(slow))
merge(self, l1: ListNode, l2: ListNode) -> ListNode:
curr = res = ListNode()
while l1 != None and l2 != None:
    if l1.val < l2.val:
        curr.next = l1
        l1 = l1.next
    else:
        curr.next = l2
        l2 = l2.next
    curr = curr.next
if l1 is None:
    curr.next = l2
if l2 is None:
    curr.next = l1
return res.next
```

