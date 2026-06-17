import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    
    results = []
    for i in range(1, t + 1):
        n = int(input_data[i])
        array = [str(2 * j + 1) for j in range(n)]
        results.append(" ".join(array))
        
    print("\n".join(results))

if __name__ == '__main__':
    solve()
