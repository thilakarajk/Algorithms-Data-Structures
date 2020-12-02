class Stack(list):

    def __init__(self):
        self.element = []

    def empty(self) -> bool:
        return len(self.element) == 0

    def push(self, ele):
        self.element.append(ele)

    def pop(self):
        return self.element.pop()

    def peek(self) -> str:
        if len(self.element) > 0:
            return self.element[len(self.element) - 1]
        else:
            raise IndexError("list index out of range")

    @property
    def size(self) -> int:
        return len(self.element)

    def __str__(self) -> str:
        return f'{self.element}'


if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(40)
    print(stack.size)
    print(stack.empty())
    print(stack)
    stack.pop()
    print(stack)
