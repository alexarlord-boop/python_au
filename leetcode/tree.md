# TREE

+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
<!---->
## Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

```python
res = list()
def dfs(root):
    if not root:
        return None
    dfs(root.left)
    res.append(root.val)
    dfs(root.right)
    return res
return dfs(root)
```

