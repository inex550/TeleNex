from typing import Optional
from . import TeleObj, Field

from .photo_size import PhotoSize


class Document(TeleObj):
    file_id: str = Field()
    file_unique_id: str = Field()
    thumb: Optional[PhotoSize] = Field(PhotoSize)
    file_name: Optional[str] = Field()
    mime_type: Optional[str] = Field()
    file_size: Optional[int] = Field()