from g.core.error import GError

class Result:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        def fmt(v):
            if isinstance(self.value, int):
                return f'_{abs(v)}'
            return str(v)
        if isinstance(self.value, list):
            return ' '.join(fmt(v) for v in self.value)
        return str(self.value)

    def __str__(self):
        return self.__repr__()