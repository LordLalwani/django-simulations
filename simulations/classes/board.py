from dataclasses import dataclass, field
from itertools import count
from typing import Optional
from manufacturerList import ManufacturerList

@dataclass()
class Board():
    name: str
    manufacturer: str
    pin_size: int
    debugger_available: Optional[bool] = False;
    id: int = field(default_factory=count().__next__, init=False)

    def __post_init__(self):
        if(self.manufacturer == ManufacturerList.ATMEL):
            self.debugger_available = True;

    def __repr__(self):
        return f"ID:{self.id:2}   |   {self.name:10} |   {self.manufacturer:40}  |   ({self.pin_size})"


ATMEGA328P = Board(name="ATMEGA328P", manufacturer=ManufacturerList.ATMEL, pin_size=16);
MPU6050 = Board(name="MPU6050",manufacturer=ManufacturerList.TEXAS_INSTRUMENTS, pin_size=6);

print(ATMEGA328P)
print(MPU6050)
