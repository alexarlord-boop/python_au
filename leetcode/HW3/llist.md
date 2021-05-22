# HW3/LLIST

+ [Merge k Sorted Lists](#merge-k-sorted-lists)
<!---->
## Merge k Sorted Lists

https://leetcode.com/problems/merge-k-sorted-lists/

```python
pointers = []
for el in lists:
    pointers.append(el)
arr = []
for i, el in enumerate(pointers):
    if el is not None:
        arr.append((el.val, i))
heapq.heapify(arr)
head, tail = None, None
while len(arr) != 0:
    helper = heapq.heappop(arr)
    i = helper[1]
    if head is None:
        head = pointers[i]
        tail = head
    else:
        tail.next = pointers[i]
        tail = tail.next
    pointers[i] = pointers[i].next
    if pointers[i] is not None:
        heapq.heappush(arr, (pointers[i].val, i))
return head
```

