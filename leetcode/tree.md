# TREE

+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
<!---->
## Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

```python
q = []
def dfs(root):
    if not root:
        return
    if root.left:
        dfs(root.left)
    q.append(root.val)
    if root.right:
        dfs(root.right)
dfs(root)
q = list(sorted(q))
return q[k - 1]
```

