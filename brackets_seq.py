n = int(input())
z = int(input())

s = [''] * (2 * n)
out_n = 0


def rec(idx, bal):
    if bal > n:
        return
    if idx == 2 * n:
        if bal == 0:
            out()
        return
    if bal < n:
        s[idx] = '('
        rec(idx + 1, bal + 1)
    if bal == 0:
        return
    s[idx] = ')'
    rec(idx + 1, bal - 1)


def out():
    global out_n
    out_n += 1
    if z == 0 or out_n == z:
        print(''.join(s))


rec(0, 0)
