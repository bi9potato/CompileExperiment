import collections

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = collections.deque([])


    def push(self, x):
        """
        self.stack = []
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        q = self.stack
        for i in range(len(q) - 1):
            q.append(q.popleft())


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack.popleft()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.stack) == 0:
            return True
        else:
            return False