# TREE

+ [Validate Binary Search Tree](#validate-binary-search-tree)
<!---->
## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

```python
global is_valid
is_valid = True
def dfs(root, low, high):
    global is_valid
    if not root:
        return
    # print(low, root.val, high)
    if (low < root.val) and (root.val < high):
        dfs(root.left, low, root.val)
        dfs(root.right, root.val, high)
    else:
        is_valid = False
dfs(root, -2**31 - 1, 2**31)
return is_valid
```

