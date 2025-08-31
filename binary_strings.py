from itertools import combinations

def generate_binary_strings_with_k_ones(n, k):
    """Generate all binary strings of length n with exactly k ones in lexicographic order"""
    strings = []
    
    # Generate all combinations of positions where 1s should be placed
    for positions in combinations(range(n), k):
        # Create binary string
        binary_str = ['0'] * n
        for pos in positions:
            binary_str[pos] = '1'
        strings.append(''.join(binary_str))
    
    # Sort to ensure lexicographic order
    strings.sort()
    return strings

def has_exactly_k_consecutive_ones(s, k):
    """Check if string has exactly one group of k consecutive ones"""
    # Find all groups of consecutive 1s
    groups = []
    i = 0
    while i < len(s):
        if s[i] == '1':
            count = 0
            start = i
            while i < len(s) and s[i] == '1':
                count += 1
                i += 1
            groups.append(count)
        else:
            i += 1
    
    # Check if there's exactly one group and it has k ones
    return len(groups) == 1 and groups[0] == k

def solve(n, k):
    # Generate all binary strings with k ones
    all_strings = generate_binary_strings_with_k_ones(n, k)
    
    # Filter strings with exactly k consecutive ones
    consecutive_strings = [s for s in all_strings if has_exactly_k_consecutive_ones(s, k)]
    
    return all_strings, consecutive_strings

if __name__ == "__main__":
    # Read input
    n, k = map(int, input().split())
    
    # Solve
    all_strings, consecutive_strings = solve(n, k)
    
    # Output
    print(' '.join(all_strings))
    print(' '.join(consecutive_strings))