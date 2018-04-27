def now():
    print('2018-04-10')


f = now
f()
print(f.__name__)


def ano(x):
    return x * x


print(ano(10))


def multi_retu():
    return 1, 2


x, y = multi_retu()
print("%d:%d", x, y)


def log(msg):
    def decorator(func):
        def wrapper(*s, **d):
            print("call func %s" % func.__name__)
            return func(*s, **d)
    return wrapper


return decorator


@log
def abc(j):
    print("print %s", j)


abc("wrapper")
