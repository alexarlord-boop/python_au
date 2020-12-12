# TREE

+ [Invert Binary Tree](#invert-binary-tree)
<!---->
## Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/

```python
def invert(root):
    if not root:
        return
    root.left, root.right = root.right, root.left
    invert(root.left)
    invert(root.right)
invert(root)
return root
```

