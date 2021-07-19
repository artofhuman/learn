# inp = "{{{**[][][]"
inp = input()

stack = []
stack2 = []
start_brackets = ['(', '[', '{']
end_brackents  = [')', ']', '}']


# stack2 = [1, ]
def check(string):
    def result(expr, pos):
        return {"result": expr, "position": pos}

    position = 0

    for ch in string:
        position += 1

        if ch in start_brackets:
            stack.append(ch)
            stack2.append(position)
        elif ch in end_brackents:
            if len(stack) == 0:
                return result(False, position)
            top = stack.pop();
            if top != start_brackets[end_brackents.index(ch)]:
                return result(False, position)
            else:
                stack2.pop()

    if len(stack) == 0:
        return result(True, 0)
    else:
        return result(False, stack2.pop())

result = check(inp)
if result['result']:
    print('Success')
else:
    print(result['position'])
