from . import (
    TeleObj,
    Field
)

class MaskPosition(TeleObj):
    point: str = Field()
    x_shift: float = Field()
    y_shift: float = Field()
    scale: float = Field()
