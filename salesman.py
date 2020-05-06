file = open('salesman.in')
lines = file.readlines()

n = int(lines.pop(0))
ls = []
p = [0] * n

used = [False] * n
min_sum = float('inf')

print(n)

for line in lines:
    ls.append(list(map(int, line.split(' '))))


def rec(idx, cur_len):
    global min_sum
    if cur_len > min_sum:
        return

    if idx == n:
        cur_sum = cur_len + ls[p[idx - 1]][0]
        if cur_sum < min_sum:
            min_sum = cur_sum
            print(p)
        return

    for i in range(1, n):
        if used[i]:
            continue
        p[idx] = i
        used[i] = True
        rec(idx + 1, cur_len + ls[p[idx - 1]][i])
        used[i] = False


rec(1, 0)
print(min_sum)
