n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))

