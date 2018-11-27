def recursive_fibonacci(last):
    for i in range(0, last):
        print(str(i) + ": " + str(fibonacci_aux(i)))

def fibonacci_aux(n):
    if(n <= 1):
        return n
    return(fibonacci_aux(n-1) + fibonacci_aux(n-2))

recursive_fibonacci(100)
