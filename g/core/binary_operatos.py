from g.core.error import GValueError


def toList(x):
    return x if isinstance(x, list) else [x]

def maskFilter(mask, ls):
    """return a list of elements from the list using the mask"""
    if len(mask) != len(ls):
        raise GValueError("lists of different length")
    out = []
    for n, elem in zip(mask, ls):
        out.extend([elem] * n)
    return out    

def concat(x, y):
    return toList(x) + toList(y)

def listIndexes(idxs, ls):
    """return a list of indexes for the given list"""
    idxs, ls = toList(idxs), toList(ls)
    result = []
    for idx in idxs:
        if idx < -len(ls) or idx >= len(ls):
            raise GValueError(f"index error")
        result.append(ls[idx])
    return result

# switch for arithmetic operations
BINARYOPS_SWITCH = {
    '+': lambda x,y: x + y,
    '-': lambda x,y: x - y,
    '*': lambda x,y: x * y,
    '%': lambda x,y: x / y,
    '|': lambda x,y: y % x,
    '^': lambda x,y: x ** y,
    '>=': lambda x,y: int(x >= y),
    '<=': lambda x,y: int(x <= y),
    '<>': lambda x,y: int(x != y),
    '>': lambda x,y: int(x > y),
    '<': lambda x,y: int(x < y),
    '=': lambda x,y: int(x == y),
    ',': concat,
    '@:': lambda f,g: lambda x: f(g(x)),
    '#': maskFilter,
    '{': listIndexes,
}

BINARYOPS_NO_LIFT = {
    '{',
    '#',
    ',',
    '@:',
}