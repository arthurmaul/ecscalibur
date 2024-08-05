from ctypes import Structure as Struct
from ctypes import c_uint16 as U16
from ctypes import c_uint32 as U32
from uuid import uuid4 as ID

class Identifier(Struct):
    _fields_ = [
        ('value', U32),
        ('gen',   U16),
        ('flags', U16)]

    def __str__(self):
        return f'{self.id} {self.generation} {self.flags}'

    def __repr__(self):
        return f'{self.to_int()}'

    def __init__(self, id=None, generation=None, flags=None):
        self.id = id or ID().int
        self.gen = gen or 0
        self.flags = flags or 0

    @classmethod
    def from_int(cls, value):
        data = cls()
        data.id = value >> 32
        data.generation = (value >> 16) & 0xFFFF
        data.flags = value & 0xFFFF
        return data

    def to_int(self):
        return (self.id << 32) + (self.generation << 16) + self.flags


i = Identifier()
print(i.value)
