file = open('request2.in')
lines = file.read().splitlines()

n = int(lines.pop(0))
ls = list(map(lambda line: tuple(map(int, line.split(' '))), lines))
ls.sort(key=lambda x: x[1])

count = 0
last = 0

for l, r in ls:
    if l >= last:
        last = r
        count += 1

print(count)