# TREE

+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
<!---->
## Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/

```python
res = 0
def dfs(root):
    if not root:
        return 0
    if (root.left is None and root.right is None):
        return 1
    elif root.left is None:
        return dfs(root.right) + 1
    elif root.right is None:
        return dfs(root.left) + 1
    elif not (root.left is None and root.right is None):
        return max(dfs(root.left), dfs(root.right)) + 1
return dfs(root)
```

