# 装饰器实现单实例模式
def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton 
class MyClass:
    pass


##################
# __new__ 与 __init__ 的关系
class Foo(object):
    def __new__(cls, name):
        print('trace __new__')
        return super().__new__(cls)
    
    def __init__(self, name):
        print('trace __init__')
        super().__init__()
        self.name = name

bar = Foo('test')
bar.name


#相当于在执行下面的操作
bar = Foo.__new__(Foo, 'test')
if isinstance(bar, Foo):
    Foo.__init__(bar, 'test')

############################
# __new__ 方式实现单例模式
class Singleton2(object):
	__isinstance = False  # 默认没有被实例化
	def __new__(cls, *args, **kwargs):
		if cls.__isinstance:  
			return cls.__isinstance  # 返回实例化对象
		cls.__isinstance = object.__new__(cls)  # 实例化
		return cls.__isinstance


