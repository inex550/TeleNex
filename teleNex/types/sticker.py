from teleNex.teleNex.types import mask_position
from typing import Optional

from . import (
    TeleObj, 
    Field,
    PhotoSize,
    MaskPosition
)


class Sticker(TeleObj):
    file_id         : str = Field()
    file_unique_id  : str = Field()
    width           : int = Field()
    height          : int = Field()
    is_animated     : bool = Field()
    thumb           : Optional[PhotoSize] = Field(PhotoSize)
    emoji           : Optional[str] = Field()
    set_name        : Optional[str] = Field()
    mask_position   : Optional[MaskPosition] = Field(MaskPosition)
    file_size       : Optional[int] = Field()