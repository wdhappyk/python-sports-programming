file = open('correct_brackets_set.in')

for line in file.read().splitlines():
    stack = []
    for i in line:
        if len(stack) > 0:
            lst_el = stack[-1]
            if i == ']' and lst_el == '[' or i == ')' and lst_el == '(':
                stack.pop()
                continue
        stack.append(i)
    print(stack)
