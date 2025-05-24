from g.core.error import GError


class Result:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        if isinstance(self.value, list):
            return f" ".join([str(v) for v in self.value])
        return str(self.value)
    
    def __str__(self):
        if isinstance(self.value, list):
            return f" ".join([str(v) for v in self.value])
        return str(self.value)