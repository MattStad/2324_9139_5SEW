"""
>>> print(subtask3((1, 4, 7, 8, 12, 14, 16, 18), 5))
False
>>> print(subtask3((1, 4, 7, 8, 12, 14, 16, 18), 16))
True
>>> print(subtask3((1, 4, 7, 8, 12, 14, 16, 18), 2))
False
>>> print(subtask3((1, 4, 7, 8, 12, 14, 16, 18), 18))
True
>>> print(subtask3((1, 4, 7, 8, 12, 14, 16, 18), 0))
False
>>> print(subtask3((1, 4, 7, 8, 12, 14, 16, 18), 1))
True
>>> print(subtask3((1, 4, 7, 8, 12, 14, 16, 18), 2000))
False
>>> print(subtask3((1, 4, 7, 8, 12, 14, 16, 18), 7))
True
"""


def subtask3(v, x):
    high = len(v)
    low = 0
    while high >= low:
        #print(f"{low} : {high}")
        mid = (high + low) // 2
        if x == v[mid]:
            return True
        elif x < v[mid]:
            if high == mid:
                return False
            high = mid
        else:
            if low == mid:
                return False
            low = mid
    return False


def subtask3_normal(v, x):
    if x in v:
        return True
    else:
        return False


