"""
Problem Name: Red Light, Green Light

Problem Statement:
Sang-Woo advises Gi-Hun to hide behind someone to avoid getting shot.
Gi-Hun follows Sang-Woo's advice and hides behind Ali, who saved his life earlier.
Gi-Hun and Ali both have the same height, K.

There are N players standing between Gi-Hun and Ali in a straight line, with the
i-th player having height H[i]. Gi-Hun wants to know the minimum number of players
who need to get shot so that Ali is visible in his line of sight.

Notes:
- Line of sight is a straight line drawn between the topmost point of two objects.
- Ali is visible if nobody between them crosses this line (H[i] <= K is fine, H[i] > K blocks).

Input Format:
- First line contains integer T (number of test cases).
- For each test case:
    - First line contains two integers: N (number of players) and K (height of Gi-Hun & Ali).
    - Second line contains N space-separated integers representing the heights of the players.

Output Format:
- For each test case, output in a single line the minimum number of players who need to get shot.

Constraints:
- 1 <= T <= 10^5
- 1 <= N <= 10^5
- 1 <= K <= 10^6
- 1 <= H[i] <= 10^6
- Sum of N over all test cases <= 5 * 10^5

Sample Input:
3
4 10
2 13 4 16
5 8
9 3 8 8 4
4 6
1 2 3 4

Sample Output:
2
1
0
"""
  

    # cook your dish here
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(T):
        N = int(input_data[idx])
        K = int(input_data[idx + 1])
        idx += 2
        
        # Read the N heights and count elements strictly greater than K
        heights = input_data[idx : idx + N]
        idx += N
        
        ans = sum(1 for h in heights if int(h) > K)
        out.append(str(ans))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()
