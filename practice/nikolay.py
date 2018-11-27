import time

def recursive_fibonacci(last):
    for i in range(0, last):
        print(str(i) + ": " + str(fibonacci_aux(i)))

def fibonacci_aux(n):
    if(n <= 1):
        return n
    return(fibonacci_aux(n-1) + fibonacci_aux(n-2))

def iterative_fib(n):
    first_num, second_num = 0, 1
    for i in range(0, n+1):
        print(str(i) + ": " + str(first_num))
        first_num, second_num = second_num, first_num + second_num

calculated = {}
def retrieve_fib(n):
    if n not in calculated.keys():
        calculated[n] = memoized_fib(n)
    return calculated[n]

def memoized_fib(n):
    if n < 2:
        return n
    else:
        return retrieve_fib(n-1) + retrieve_fib(n-2)




startTime = int(time.time()*1000.0)
memoized_fib(101)
for i in calculated.items():
    print(str(i[0]) + ": " + str(i[1]))
endTime = int(time.time()*1000.0)
print("Memoized recursive time: " + str(endTime - startTime))

startTime = int(time.time()*1000.0)
iterative_fib(100)
endTime = int(time.time()*1000.0)
iterative_time = endTime - startTime

print("Iterative time: " + str(iterative_time))

startTime = int(time.time()*1000.0)
recursive_fibonacci(100)
endTime = int(time.time()*1000.0)
recursive_time = endTime - startTime

print("Recursive time: " + str(recursive_time))
