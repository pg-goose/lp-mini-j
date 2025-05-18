UNARYOPS_SWITCH = {
    '_': lambda x: -x,
    'i.': lambda x: list(range(x)), # TODO investigate if we can leave only range for lazy evaluation
    '#': lambda x: len(x),
    ']': lambda x: x,
}
