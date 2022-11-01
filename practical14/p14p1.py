num = int(input("Please enter a positive integer to calculate the factorial: "))
#non recursive
import time

def nonrecur(x):
    a = 1
    i = 1
    while i <= x:
        a *= i
        i += 1
    return(a)
start = time.time()
print(nonrecur(num))
end = time.time()
print((end - start)* 1000)
#recursive
def recur(x):
    if x == 0:
        return 1
    else:
        return (x * recur(x- 1))
rstart = time.time()
print(recur(num))
rend = time.time()
print((rend - rstart) * 1000)