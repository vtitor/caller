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

        if hasattr(value, '__call__'):
            value.__call__ = fcall
            return value

        _type = Bool if type(value) is types.BooleanType else type(value)
        return type('Callable', (_type,), {'__call__': fcall})(value)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.fcall, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.fcall, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.fcall, self.__doc__)

    def caller(self, fcall):
        return type(self)(self.fget, self.fset, self.fdel, fcall, self.__doc__)


class Bool(object):
    def __init__(self, value):
        if not isinstance(value, bool):
            raise ValueError
        self.value = value

    def __bool__(self):
        return self.value

    __nonzero__ = __bool__
