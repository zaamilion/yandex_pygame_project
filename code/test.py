res = set()

for _ in range(int(input())):
    num = int(input())
    num_r = str(num)[::-1]
    num_s = int(num_r[-2:])
    res.add(num_s)
res = list(res)
res.sort()
print(*res)
