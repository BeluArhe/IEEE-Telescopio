import sys
import bisect

def main():
    input = sys.stdin.read().split()
    n = int(input[0])
    
    stars = []
    idx = 1
    for _ in range(n):
        s = int(input[idx]); f = int(input[idx+1]); d = int(input[idx+2])
        idx += 3
        stars.append((s, f, d))
    
    # Sort by finish time
    stars.sort(key=lambda x: x[1])
    
    finish_times = [star[1] for star in stars]
    desirabilities = [star[2] for star in stars]
    
    dp = [0] * n
    dp[0] = desirabilities[0]
    for i in range(1, n):
        pos = bisect.bisect_left(finish_times, stars[i][0]) - 1
        prev_dp = dp[pos] if pos >= 0 else 0
        dp[i] = max(dp[i-1], prev_dp + desirabilities[i])
    
    print(dp[-1])

if __name__ == "__main__":
    main()