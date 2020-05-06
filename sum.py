n = int(input())
a = {}
z = int(input())
out_n = 0


def rec(idx, sum, last):
    if sum == n:
        out(idx)
        return

    for i in range(last, n - sum + 1):
        a[idx] = i
        rec(idx + 1, sum + i, i)


def out(idx):
    global out_n
    out_n += 1
    if z == 0 or out_n == z:
        res = [a[i] for i in range(idx)]
        print(str(n) + ' = ' + ' + '.join(map(str, res)))


rec(0, 0, 1)
