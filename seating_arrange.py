import sys

def solve():
    # Fast I/O reading all input tokens
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        x = int(input_data[idx+1])
        s = int(input_data[idx+2])
        u = input_data[idx+3]
        idx += 4
        
        x_cap = min(x, n)
        
        dp = [set() for _ in range(x_cap + 1)]
        dp[x_cap].add(0) # Initially, all capped tables are empty, and 0 slots are available
        
        for char in u:
            next_dp = [set() for _ in range(x_cap + 1)]
            
            for r in range(x_cap + 1):
                for slots in dp[r]:
                    # Option 1: Kick out the person (State remains unchanged)
                    next_dp[r].add(slots)
                    
                    if (char == 'I' or char == 'A') and r > 0:
                        # Cap the slots at n because we can never use more slots than the remaining people
                        next_dp[r - 1].add(min(n, slots + s - 1))
                        
                    if (char == 'E' or char == 'A') and slots > 0:
                        next_dp[r].add(slots - 1)
                        
            dp = next_dp
            
        max_seated = 0
        for r in range(x_cap + 1):
            for slots in dp[r]:
                seated = (x_cap - r) * s - slots
                if seated > max_seated:
                    max_seated = seated
                    
        out.append(str(max_seated))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()

