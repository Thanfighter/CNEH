# Distance Vector Routing Algorithm

n = int(input("Enter number of nodes: "))

print("Enter cost matrix (999 for no connection):")

cost = []

for i in range(n):
    cost.append(list(map(int, input().split())))

dist = [row[:] for row in cost]

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j],
                             dist[i][k] + dist[k][j])

print("Shortest distance matrix:")

for row in dist:
    print(*row)


'''
SAMPLE INPUT:
Enter number of nodes: 3
Enter cost matrix (999 for no connection):
0 2 7
2 0 1
7 1 0

SAMPLE OUTPUT:
Shortest distance matrix:
0 2 3
2 0 1
3 1 0
'''