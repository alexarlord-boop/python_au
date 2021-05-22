# HW3/DESIGN

+ [Min Stack](#min-stack)
+ [Implement Queue using Stacks](#implement-queue-using-stacks)
+ [Implement Stack using Queues](#implement-stack-using-queues)
+ [Design Twitter](#design-twitter)
<!---->
## Min Stack

https://leetcode.com/problems/min-stack/

```python
def __init__(self):
    """
    initialize your data structure here.
    """
    self.stack = []
def push(self, val: int) -> None:
    min_val = self.getMin()
    if min_val == None or val < min_val:
        min_val = val
    self.stack.append((val, min_val))
def pop(self) -> None:
    return self.stack.pop()
def top(self) -> int:
    return self.stack[-1][0]
def getMin(self) -> int:
    if not self.stack:
        return None
    else:
        return self.stack[-1][1]

```

## Implement Queue using Stacks

https://leetcode.com/problems/implement-queue-using-stacks/

```python
def __init__(self):
    self.lst = []
def push(self, x):
    self.lst.append(x)
def pop(self):
    if len(self.lst) > 0:
        return self.lst.pop()
def peek(self):
    if len(self.lst) > 0:
        return self.lst[-1]
def empty(self):
    return len(self.lst) == 0
s MyQueue:
def __init__(self):
    self.P = Stack()
    self.Q = Stack()
def _QtoP(self):
    if self.P.empty():
        while not self.Q.empty():
            self.P.push(self.Q.pop())
def push(self, x: int) -> None:
    self.Q.push(x)
def pop(self) -> int:
    self._QtoP()
    return self.P.pop()
def peek(self) -> int:
    self._QtoP()
    return self.P.peek()
def empty(self) -> bool:
    return self.P.empty() and self.Q.empty()
```

## Implement Stack using Queues

https://leetcode.com/problems/implement-stack-using-queues/

```python
def __init__(self):
    """
    Initialize your data structure here.
    """
    self.q1 = deque()
    self.q2 = deque()
    self.tops = None
def push(self, x: int) -> None:
    """
    Push element x onto stack.
    """
    self.q1.appendleft(x)
    self.tops = x
def pop(self) -> int:
    """
    Removes the element on top of the stack and returns that element.
    """
    while len(self.q1) > 1:
        self.tops = self.q1.pop()
        self.q2.appendleft(self.tops)
    res = self.q1.pop()
    temp = self.q1
    self.q1 = self.q2
    self.q2 = temp
    return res
def top(self) -> int:
    """
    Get the top element.
    """
    return self.tops
def empty(self) -> bool:
    """
    Returns whether the stack is empty.
    """
    return not self.q1 and not self.q2
```

## Design Twitter

https://leetcode.com/problems/design-twitter/

```python
def __init__(self):
    self.x = 0
    self.t = defaultdict(list)
    self.f = defaultdict(set)

def postTweet(self, uid: int, tid: int) -> None:
    self.x += 1;self.t[uid].append((self.x, tid))

def getNewsFeed(self, uid: int) -> List[int]:
    m = self.t[uid].copy()
    for _uid in self.f[uid]: m.extend(self.t[_uid])
    return [x[1] for x in sorted(m, key=lambda x: -x[0])][:10]

def follow(self, fid: int, feid: int) -> None:
    self.f[fid].add(feid)

def unfollow(self, fid: int, feid: int) -> None:
    if feid in self.f[fid]: self.f[fid].remove(feid)```

