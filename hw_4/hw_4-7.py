def fibo_gen(a):
    b = 1
    for i in range(1, a):
        if i > 15:
            break
        b *= i
        yield b
for i in fibo_gen(10):
    print(i)