from collections import deque

def bfs(X, Y, N, puddles):
    queue = deque([(0, 0, 0)])  # (x, y, distance)
    visited = set()

    while queue:
        x, y, distance = queue.popleft()

        if (x, y) == (X, Y):
            return distance

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx <= X and 0 <= ny <= Y and (nx, ny) not in puddles:
                queue.append((nx, ny, distance + 1))

    return -1  # 목적지에 도달할 수 없는 경우

# 입력 받기
X, Y, N = map(int, input().split())
puddles = set(tuple(map(int, input().split())) for _ in range(N))

# 최단 경로에서 웅덩이를 피하면서 목적지에 도달하는 최소 거리 출력
result = bfs(X, Y, N, puddles)
print(result)


