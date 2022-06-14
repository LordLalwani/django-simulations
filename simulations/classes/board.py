from dataclasses import dataclass, field
from itertools import count
from typing import Optional
from manufacturerList import ManufacturerList

@dataclass()
class Board():
    manufacturer: str
    pin_size: int
    debugger_available: Optional[bool] = False;
    id: int = field(default_factory=count().__next__, init=False)

    def __post_init__(self):
        if(self.manufacturer == ManufacturerList.ATMEL):
            self.debugger_available = True;


ATMEGA328P = Board(manufacturer=ManufacturerList.ATMEL, pin_size=16);
MPU6050 = Board(manufacturer=ManufacturerList.TEXAS_INSTRUMENTS, pin_size=6);

print(ATMEGA328P)
print(MPU6050)
