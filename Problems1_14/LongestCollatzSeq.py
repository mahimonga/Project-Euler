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
    collatz_lens = [collatz_seq_len(num) for num in range(1, n + 1)]
    return collatz_lens.index(max(collatz_lens)) + 1

def problem14():
    return longest_collatz_end(1000000)
    