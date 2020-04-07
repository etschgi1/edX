def fib(n):
    '''dumb recursive fib'''
    if n == 0 or n == 1:
        return 1
    else:
        return(fib(n-2)+fib(n-1))


# print(fib(35))


def fastfib(n, stored={}):
    '''faster fib calc'''
    if n == 0 or n == 1:
        return 1
    else:
        if n in stored:
            return stored[n]
        else:
            result = (fastfib(n-1, stored)+fastfib(n-2, stored))
            stored[n] = result
            return result


for i in range(50):
    print("Fib number: "+str(i))
    print(fib(i))
