def even_nums_generator(n):
    for i in range(2, n+1, 2):
        yield i

for i in even_nums_generator(10):
    print(i)