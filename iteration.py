n = int(input())  # длина элементов
m = int(input())  # кол-во элементов
z = int(input())  # под каким номером элемент нужно вывести - 0 = все

a = [i for i in range(n)]
out_n = 0


def rec(idx):
    if idx == n:
        out()
        return

    for i in range(1, m + 1):
        a[idx] = i
        rec(idx + 1)


def out():
    global out_n
    out_n += 1
    if z == 0 or out_n == z:
        print(' '.join(map(str, a)))


rec(0)
