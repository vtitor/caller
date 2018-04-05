import pickle
import copy

from caller import property


class Example(object):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


def test_property():
    example = Example(1)
    assert example.value == 1
    example.value += 7
    assert example.value == 8
    example.value(548)
    assert example.value == 548


def test_pickle():
    example = {Example(5).value: 8}
    pickled_example = pickle.dumps(example)
    assert pickle.loads(pickled_example) == {5: 8}


def test_deepcopy():
    example = Example({5: 8})
    clone = copy.deepcopy(example)
    assert example.value == clone.value
    assert example.value is not clone.value


def test_assign_properties():
    first_example = Example(1)
    second_example = Example(2)
    first_example.value = second_example.value
    first_example.value(4)
    second_example.value(8)
    assert first_example.value == 4
    assert second_example.value == 8
