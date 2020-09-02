from enum import IntEnum

class PriorityTypes(IntEnum):
    TOP = 1
    MIDDLE = 2
    BOTTOM = 3
    
    @classmethod
    def choices(cls):
        print(list(key for key in cls))
        return [(key.value, key.name) for key in cls]


