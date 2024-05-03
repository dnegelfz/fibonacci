import time
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


#Q1
recur_times = []
dp_times = []

max_n = 100
plt.figure(figsize=(10, 5))
plt.ion()
plt.show()
for i in range(1, max_n+1):
    start_time = time.time()
    recurf(i)
    recur_times.append(time.time() - start_time)

    start_time = time.time()
    dpf(i)
    dp_times.append(time.time() - start_time)
    print(f'maximum value of n:{i}')

    plt.clf()
    plt.plot(range(1, i+1), recur_times, label='Recursive')
    plt.plot(range(1, i+1), dp_times, label='Dynamic Programming')
    plt.title('Execution Time for Fibonacci Sequence')
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.grid(True)
    plt.draw()
    plt.pause(0.5)

plt.ioff()
plt.show()
