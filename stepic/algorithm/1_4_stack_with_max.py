import sys

class StackWithMax:
    def __init__(self):
        self.max_stack = []
        self.stack = []

    def push(self, value):
        value = int(value)

        if self.is_empty():
            self.max_stack.append(value)
        else:
            max_val = self.max()
            if max_val > value:
                self._set_max(max_val)
            else:
                self._set_max(value)

        self.stack.append(value)

    def _set_max(self, value):
        self.max_stack.append(value)

    def max(self):
        return self.max_stack[-1]

    def pop(self):
        self.max_stack.pop()
        self.stack.pop()

    def is_empty(self):
        return not self.stack


q = int(next(sys.stdin))

stack = StackWithMax()

for line in sys.stdin:
    cmd = line.split()

    if 'push' == cmd[0]:
        stack.push(cmd[1])
    elif 'pop' == cmd[0]:
        stack.pop()
    elif 'max' == cmd[0]:
        print(stack.max())
