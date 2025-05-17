def maskFilter(mask, ls):     
    if len(mask) != len(ls):
        raise ValueError("lists of different length")
    return [x for m, x in zip(mask, ls) if m]

def concat(x, y):
    xl = x if isinstance(x, list) else [x]
    yl = y if isinstance(y, list) else [y]
    return xl + yl

# switch for arithmetic operations
BINARYOPS_SWITCH = {
    '+': lambda x,y: x + y,
    '-': lambda x,y: x - y,
    '*': lambda x,y: x * y,
    '%': lambda x,y: x / y,
    '|': lambda x,y: x % y,
    '^': lambda x,y: x ** y,
    '>=': lambda x,y: x >= y,
    '<=': lambda x,y: x <= y,
    '<>': lambda x,y: x != y,
    '>': lambda x,y: x > y,
    '<': lambda x,y: x < y,
    '=': lambda x,y: x == y,
    ',': concat,
    '@:': lambda f,g: lambda x: f(g(x)),
    '#': maskFilter,
    '{': lambda idxs,ls: [ls[i] for i in idxs],
}