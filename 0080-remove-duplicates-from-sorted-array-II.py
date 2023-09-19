n = list(map(int, input().split()))

for i in n:
    if n.count(i) > 2:
        n.remove(i)
        n.append('_')

print(n)