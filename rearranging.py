n = int(input())
z = int(input())  # под каким номером элемент нужно вывести - 0 = все

a = [i for i in range(n)]
used = [False for i in range(0, n + 1)]
out_n = 0


def rec(idx):
    if idx == n:
        out()
        return

    for i in range(1, n + 1):
        if used[i]:
            continue
        a[idx] = i
        used[i] = True
        rec(idx + 1)
        used[i] = False


def out():
    global out_n
    out_n += 1
    if z == 0 or out_n == z:
        print(' '.join(map(str, a)))


rec(0)
