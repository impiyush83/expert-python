def memoize(f):
    memo = {}

    def helper(x, string):
        # always 1 is printed as string
        if x not in memo:
            memo[x] = f(x, string)
            # goes through callback stack
        # finally returns memo {1: 1, 0: 0, 2: 1, 3: 2, 4: 3} for n = 5 of x memo[x]. # returned required answer
        return memo[x]
    return helper


@memoize
def fib(n, string):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1, "1") + fib(n - 2, "2")


print(fib(8, "try"))
