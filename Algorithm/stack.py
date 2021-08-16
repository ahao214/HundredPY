class Stack:
    def __init__(self):
        self.stack = []

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def isEmpty(self):
        return len(self.stack) == 0


# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(4)
# print(stack.pop())


def brace_match(s):
    match = {'}': '{', ']': '[', ')': '('}
    stack = Stack()
    for ch in s:
        if ch in {'(', '[', '{'}:
            stack.push(ch)
        else:
            if stack.isEmpty():
                return False
            elif stack.get_top() == match[ch]:
                stack.pop()
            else:
                return False

    if stack.isEmpty():
        return True
    else:
        return False


print(brace_match('[][](){}{}'))
print(brace_match('[[[](()]]][[{{}}}()'))