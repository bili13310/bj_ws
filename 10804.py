import sys

card = [x+1 for x in range(20)]

for _ in range(10):
    start, end = map(int, sys.stdin.readline().split())
    card = card[:start-1] + list(reversed(card[start-1:end])) + card[end:] # [::-1]

print(*card)