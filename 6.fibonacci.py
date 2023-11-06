# for loop
n=int(input('Enter a number:'))
a,b=0,1
for i in range(n):
    a,b=b,a+b
    print(a)
# while loop
i=0
while i<n:
    a,b=b,a+b
    print(a)
    i+=1

# start and end range

def fibonacci_range(start,end):
    fib_list=[0,1]
    for i in range(2,end+1):
        fib_list.append(fib_list[i-1]+fib_list[i-2])
    return fib_list[start:end+1]
start=10
end=16
result=fibonacci_range(start=10,end=16)
print(f'Fibonacci series between {start} and {end}:{result}')


# recursive

def rec_fib(n):
    if n==0:
        return []
    elif n==1:
        return [0,1]
    else:
        fib_series=rec_fib(n-1)
        fib_series.append(fib_series[-1]+fib_series[-2])
        return fib_series
print(rec_fib(10))

# recursive using loop
def rec_fib2(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return rec_fib2(n-1)+rec_fib2(n-2)
for i in range(11):
    print(rec_fib2(i),end=' ')


#print the fibonacci series from real number sequence
def fibonacci_range(start, end):
    fib_series = [0, 1]
    while fib_series[-1] <= end:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return [num for num in fib_series if start <= num <= end]

# Test the function
start = 10
end = 100
print(f"Fibonacci series between {start} and {end} is: {fibonacci_range(start, end)}")
