import types


class property(property):
    def __init__(self, fget=None, fset=None, fdel=None, fcall=None, doc=None):
        super(property, self).__init__(fget, fset, fdel, doc)
        self.fcall = fcall

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self

        if self.fget is None:
            raise AttributeError('unreadable attribute')

        if self.fcall is None and self.fset is None:
            return self.fget(obj)

        value = self.fget(obj)
        fcall = types.MethodType(self.fcall or self.fset, obj)

        _type = _Bool if type(value) is bool else type(value)
        return type('Callable', (_type, _Callable), {
            '__call__': fcall, '__cast__': _type,
            '__reduce__': lambda _: (_type, (value,))
        })(value)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")

        if isinstance(value, _Callable):
            value = _Callable.resolve(value)

        self.fset(obj, value)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.fcall, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.fcall, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.fcall, self.__doc__)

    def caller(self, fcall):
        return type(self)(self.fget, self.fset, self.fdel, fcall, self.__doc__)


class _Callable:
    @staticmethod
    def resolve(value):
        while isinstance(value, _Callable):
            value = value.__cast__(value)
        return value


class _Bool(object):
    def __init__(self, value):
        if not isinstance(value, bool):
            raise ValueError
        self.value = value

    def __bool__(self):
        return self.value

    __nonzero__ = __bool__
