import unittest


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
        if self.is_empty():
            return 0
        return self.max_stack[-1]

    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()

    def is_empty(self):
        return not self.stack

    def __repr__(self):
        return str(self.stack)

    def __len__(self):
        return len(self.stack)


class Queue(object):
    def __init__(self):
        self.instack = StackWithMax()
        self.outstack = StackWithMax()

    def enqueue(self,element):
        self.instack.push(element)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.push(self.instack.pop())
        return self.outstack.pop()

    @property
    def max(self):
        return max(self.outstack.max(), self.instack.max())


def solution(n, arr, m):
    qq = Queue()

    first_part = arr[0:m]
    result = []

    for e in first_part:
        qq.enqueue(e)

    result.append(str(qq.max))

    for e in arr[m:]:
        qq.dequeue()
        qq.enqueue(e)

        result.append(str(qq.max))

    return ' '.join(result)


if __name__ == '__main__':
    class TestSolution(unittest.TestCase):
        def test_stack_1(self):
            arr = list(map(int, '34 51 61 90 26 84 2 25 7 8 25 78 21 47 25'.split()))
            result = solution(15, arr, 3)

            expected = '61 90 90 90 84 84 25 25 25 78 78 78 47'
            self.assertEqual(result, expected)

        def test_stack_2(self):
            arr = list(map(int, '2 7 3 1 5 2 6 2'.split()))
            result = solution(8, arr, 4)

            expected = '7 7 5 6 6'
            self.assertEqual(result, expected)


TestSolution().test_stack_1()
TestSolution().test_stack_2()
