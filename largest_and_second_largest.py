"""
Largest and Second Largest
You are given an array 
A
A of 
N
N integers.
Find the maximum sum of two distinct integers in the array.

Note: It is guaranteed that there exist at least two distinct integers in the array.
"""

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    largest = max(a)
    second_largest = max(x for x in a if x != largest)

    print(largest + second_largest)
