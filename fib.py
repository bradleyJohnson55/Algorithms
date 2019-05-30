
# recursive with memoization 
fibs = [-1 for i in range(100)]

def fib(n):
    if n == 0:
        fibs[n] = 0
    elif n == 1:
        fibs[1] = 1
    else:
        if (fibs[n] != -1):
            return fibs[n]
        else:
            fibs[n] = fib(n - 1) + fib(n - 2)
            return fibs[n]
    return fibs[n]

'''
num = ''
while(num != 'quit'):
    num = input('enter a number to call fib: ' )
    print('fib(' + str(num) + ') = ' + str(fib(num)))
'''

# iterative, bottom-up
def bottomUpFib(n):
    fibs = [-1 for i in range(n + 2)]
    fibs[0] = 0
    fibs[1] = 1
    if n == 0 or n == 1:
        return fibs[n]

    for i in range(2, n + 1):
        fibs[n] = fibs[n - 1] + fibs[n - 2]

    return fibs[n]

while True:
    num = input("enter a fib number to compute")
    print('fib(' + str(num) + ') = ' + str(bottomUpFib(int(num))))          
