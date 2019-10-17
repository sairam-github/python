import collections.abc

def find_sum(values):
    if not isinstance(values, collections.abc.Iterable):
        raise TypeError('values must be of a collection type')
    else:
        sum = 0
        for v in values:
            if not isinstance(v, (int, float)):
                raise TypeError('elements must be numeric')
            sum += v
    return sum


print(find_sum([1, 12, -15]))