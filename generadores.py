def square(it):
    for i in it:
        yield i*i

def first(n, it):
     parar = 0
     for i in it:
         if parar < n:
             yield i
             parar += 1
         else:
             break

def filter(cond, it):
    for i in it:
        if cond(i):
            yield i

def take_while(cond, it):
    for i in it:
        if cond(i):
            yield i
        else:
            break

def squares():
    i = 1
    while True:
        yield i * i
        i += 1

def capicua(n):
    num_s = str(n)
    if (num_s == num_s[::-1]):
        return True

if __name__ == "__main__":
    primero = first(100, squares())
    print(list(primero))
    segundo = take_while(lambda n: n < 100, squares())
    print(list(segundo))
    tercero = first(20,filter(lambda n: capicua(n),squares()))
    print(list(tercero))