def even_n(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter your N:"))
for num in even_n(n):
    print(num)