def even(n):
    return n % 2 == 0

def next_term(n):
    return n // 2 if even(n) else 3 * n + 1

def collatz_seq_len(n):
    if n <= 2:
        return n
    if n == 4:
        return 3
    return 1 + collatz_seq_len(next_term(n))

def longest_collatz_end(n):
    max_len = 0
    end = -1
    for i in range(1, n + 1):
        if collatz_seq_len(i) > max_len:
            max_len = collatz_seq_len(i)
            end = i
    return end
        
if __name__ == '__main__':
    print(longest_collatz_end(1000000))
    