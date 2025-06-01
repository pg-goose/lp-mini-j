from g.core.error import GError

class Result:
    def __init__(self, value: any | GError):
        self.value = value

    def __repr__(self):
        def fmt(v):
            if isinstance(self.value, int):
                return f'_{abs(v)}'
            return f'{v}'
        if isinstance(self.value, list):
            return ' '.join(fmt(v) for v in self.value)

    def __str__(self):
        return self.__repr__()