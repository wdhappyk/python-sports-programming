ls = [10, 8, 2, 1]
s = 27
count = 0

for i in ls:
    count += s // i
    s %= i

print(count)
