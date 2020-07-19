
def Fib(n):
    # define the fibonacci sequence using recursion
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # The respective elements are gotten by summing the previous two elements in the sequence
        return Fib(n-1) + Fib(n-2)


list = []
total = 0
# using guess work, we find Fib(7) > 10 and Fib(13) < 200. Our range
for n in range(7, 13):
    # For the results between our range, pick out the even numbers
    if Fib(n) % 2 == 0:
        # push the even numbers to an array/list
        list.append(Fib(n))
        # sum the numbers up
        total += Fib(n)


print(
    f"The list of even Fibonacci sequence numbers between 10 and 200 is {list} ")
print(f"Their total sum is {total}")
