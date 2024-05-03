import matplotlib.pyplot as plt

f4 = 0
def recurf(n):
    global f4
    if n <= 1:
        return n
    else:
        if n == 4:
            f4 += 1
        return recurf(n-1) + recurf(n-2)

def dpf(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]

f4_times = []

max_n = 50
plt.figure(figsize=(10, 5))
plt.ion()
plt.show()
for i in range(5, max_n+1):
    recurf(i)
    f4_times.append(f4)
    f4 = 0

    plt.clf()
    plt.plot(range(5, i+1), f4_times, label='F(4) times')
    plt.title('Overlapping Subproblem: F(4) Times')
    plt.xlabel('n')
    plt.ylabel('Times')
    plt.legend()
    plt.grid(True)
    plt.draw()
    plt.pause(0.5)

plt.ioff()
plt.show()