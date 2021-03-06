W = 4
n = 2
cs = [10, 12]
ws = [2, 3]

items = []

for i in range(n):
    items.append((cs[i], ws[i]))

items.sort(key=lambda item: item[0] / item[1], reverse=True)

cur_w = 0
cur_c = 0
count = 0

for c, w in items:
    new_w = cur_w + w
    if new_w <= W:
        count += 1
        cur_w = new_w
        cur_c += c
    else:
        break

print('Items: ', count)
print('Weight: ', cur_w, '/', W)
print('Total cost: ', cur_c)
