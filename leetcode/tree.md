# TREE

+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
<!---->
## Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/

```python
if not root:
    return
res = []
q = [root]
while q:
    new_q = []
    tmp = []
    for node in q:
        if node.left:
            new_q.append(node.left)
        if node.right:
            new_q.append(node.right)
        tmp.append(node.val)
    q = new_q
    res.append(tmp)
return res
```

