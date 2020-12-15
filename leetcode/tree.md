# TREE

+ [Binary Search Tree Iterator](#binary-search-tree-iterator)
<!---->
## Binary Search Tree Iterator

https://leetcode.com/problems/binary-search-tree-iterator/

```python
def __init__(self, root: TreeNode):
    self.res = list()
    self.p = -1
    self.dfs(root)

def dfs(self, root):
    if not root:
        return
    self.dfs(root.left)
    self.res.append(root.val)
    self.dfs(root.right)

def next(self) -> int:
    self.p += 1
    return self.res[self.p]

def hasNext(self) -> bool:
    return self.p + 1 < len(self.res)
```

