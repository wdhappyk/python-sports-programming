data = []
file = open('schedule2.in')
lines = file.read().splitlines()
n = int(lines.pop(0))
for line in lines:
    if line.strip() == '':
        continue
    a, b = map(int, line.split(' '))
    data.append((a, b))

data.sort(key=lambda x: x[1], reverse=True)

used = {}
sum_v = 0

for i in range(n):
    k = data[i][0]
    while k >= 1 and used.get(k) is not None:
        k -= 1
    if k == 0:
        continue
    used[k] = True
    sum_v += data[i][1]

print(sum_v)
