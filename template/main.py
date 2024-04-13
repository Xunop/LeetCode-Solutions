import sys
import math
from collections import defaultdict, Counter
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right

# Input parsing
def get_int():
    return int(input().strip())

def get_list():
    return list(map(int, input().split()))

# Constants
MOD = 10**9 + 7
INF = float('inf')

# Math functions
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

# Data structures
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            if self.rank[pu] > self.rank[pv]:
                self.parent[pv] = pu
            elif self.rank[pu] < self.rank[pv]:
                self.parent[pu] = pv
            else:
                self.parent[pu] = pv
                self.rank[pv] += 1

# Algorithms
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def dijkstra(graph, start):
    dist = {node: INF for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cost, node = heappop(pq)
        if cost > dist[node]:
            continue
        for neighbor, weight in graph[node].items():
            if cost + weight < dist[neighbor]:
                dist[neighbor] = cost + weight
                heappush(pq, (dist[neighbor], neighbor))
    return dist

# Main function
def main():
    # Input handling
    n = get_int()
    arr = get_list()

    # Algorithm logic
    # Your code here

    # Output
    print("Hello ACM!")

if __name__ == "__main__":
    main()
