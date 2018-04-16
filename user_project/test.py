def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo # 返回的是类，不是类的实例
    else:
        class Bar(object):
            pass
        return Bar
MyClass = choose_class('foo')
print(MyClass) # 函数返回的是类，不是类的实例
# <class '__main__.choose_class.<locals>.Foo'>
print(MyClass()) # 你可以通过这个类的实例创建对象
# <__main__.choose_class.<locals>.Foo object at 0x000001BFE67CC470>

