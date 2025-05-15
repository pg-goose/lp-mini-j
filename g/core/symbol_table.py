class SymbolTable():
    """
    A simple symbol table to store variable names and their values.
    """
    def __init__(self):
        self.symbols = {}

    def define(self, name, value = None):
        self.symbols[name] = value
    
    def resolve(self, name):
        if name not in self.symbols:
            raise NameError(f"{name} not defined")
        return self.symbols[name]