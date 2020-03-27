# PEP 318 装饰器  PEP-3129 类装饰器

# 前置问题
def func1():
    pass
var = func1
var2 = func1()

# func1 表示函数
# func1() 表示执行函数


# 装饰器, @ 语法糖
@decorate   
def func():
    print('do sth')

# 等效于下面
def func():
    print('do sth')
func = decorate(func)


