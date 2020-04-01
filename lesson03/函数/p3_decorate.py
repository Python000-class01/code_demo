# func 表示函数
# func() 表示执行函数
def func(x):
    return x + 1

new = func
print(new(1))


def decorate(func):
    def inner():
        print('in decorate')
        func()
    return inner

@decorate
def target():
    print('do something')

target()

# @decorate
# def target()
# 相当于target = decorate(target)
############################################
