def closure():
    def add(a, b):
        return a + b
    return add

def evalute_closure(f, a, b):
    return f(a, b)

print(evalute_closure(closure(), 1, 2))