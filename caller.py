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

        if self.fcall is None:
            return self.fget(obj)

        value = self.fget(obj)
        callable_value = type(
            'callable_cls',
            (type(value),),
            {'__call__': types.MethodType(self.fcall, obj)}
        )(value)

        return callable_value

    def caller(self, fcall):
        return type(self)(self.fget, self.fset, self.fdel, fcall, self.__doc__)
