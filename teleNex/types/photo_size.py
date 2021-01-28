from typing import Optional
from . import TeleObj, Field


class PhotoSize(TeleObj):
    file_id: str = Field()
    file_unique_id: str = Field()
    width: int = Field()
    height: int = Field()
    file_size: Optional[int] = Field()