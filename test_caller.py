from caller import property


class Example(object):
    def __init__(self):
        self._value = 1

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @value.caller
    def value(self, value):
        self._value = value


def test_property():
    example = Example()
    assert example.value == 1

    example.value += 7
    assert example.value == 8

    example.value(548)
    assert example.value == 548
