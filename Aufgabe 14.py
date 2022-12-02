def collatz(n):
    counter = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            counter += 1
        else:
            n = 3 * n + 1
            counter += 1
        if n == 1:
            return counter


num_large = 0
seq_large = 0

for i in range(1000000,1,-1):
    n=collatz(i)
    if n > seq_large:
        num_large = i
        seq_large = n
print(num_large)
