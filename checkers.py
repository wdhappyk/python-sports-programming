n = int(input())
m = int(input())
z = int(input())

a = ['.' for i in range(n)]
out_n = 0


def rec(idx, bal, last):
    if idx == n:
        if bal == m:
            out()
        return

    if last != '*' and bal < m:
        a[idx] = '*'
        rec(idx + 1, bal + 1, '*')
    a[idx] = '.'
    rec(idx + 1, bal, '.')


def out():
    global out_n
    out_n += 1
    if z == 0 or out_n == z:
        print(''.join(a))


rec(0, 0, '.')
