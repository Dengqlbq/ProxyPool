class LazyProperty(object):
    """
    延迟绑定类
    资料：https://segmentfault.com/a/1190000005818249
    """
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        val = self.func(instance)
        setattr(instance, self.func.__name__, val)
        return val


class Singleton(type):
    """
    控制单例的元类
    资料：https://segmentfault.com/a/1190000008141049
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
