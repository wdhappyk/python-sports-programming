n = int(input())
z = int(input())  # под каким номером элемент нужно вывести - 0 = все

s = [''] * (2 * n)
out_n = 0
opening = ['(', '[']
closing = [')', ']']
els = ['(', ')', '[', ']']


def rec(idx, stack):
    if idx == 2 * n:
        if len(stack) == 0:
            out()
        return

    for i in els:
        if idx == 0 and i in closing:
            continue
        c = stack[:]
        s[idx] = i

        if len(c) > 0:
            lst_el = c[-1]
            if i == ']' and lst_el == '[' or i == ')' and lst_el == '(':
                c.pop()
                rec(idx + 1, c)
                continue

        c.append(i)
        rec(idx + 1, c)


def out():
    global out_n
    out_n += 1
    if z == 0 or out_n == z:
        print(''.join(s))


rec(0, [])
